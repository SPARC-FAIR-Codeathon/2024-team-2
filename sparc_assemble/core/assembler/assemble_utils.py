import os
import copy

from thefuzz import process
from ruamel import yaml as YAML
from sparc_assemble.core.assembler.workflow import WorkflowGenerator
from owlready2.namespace import Ontology
from sparc_assemble.core.assembler.sparql_queries import find_method_cwl
from pathlib import Path
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # A lightweight model, more available options exist

def fuzzy_match(user_input, possible_requests, threshold=80):
    # Fuzzy matching to find the closest match
    match, score = process.extractOne(user_input, possible_requests)
    if score >= threshold:
        return match
    return None

def sbert_match(user_input, possible_requests):

    query_embedding = model.encode(user_input)
    request_embeddings = model.encode(possible_requests)

    similarities = [(req, util.cos_sim([query_embedding], [emb])[0][0]) for req, emb in
                    zip(possible_requests, request_embeddings)]
    # similarities = [(req, doc.similarity(nlp(req))) for req in possible_requests]
    best_match = max(similarities, key=lambda x: x[1])

    if best_match[1] > 0.6:  # Adjust the threshold as needed
        return best_match[0]
    return None

def prompt_input_request_nlp(options: list[str]) -> str:
    """
    Prompt the user for their parameter of interest and match it to existing options if possible.:
    Args:
        options (list[str]): list of individuals that can be requested
    Returns:
         output (int): request
    """
    while True:
        # Prompt the user for their request
        request = input(f"\nPlease specify which parameter you would like to derive: ")

        match = fuzzy_match(request, options)

        if match:
            choice = input(f"Did you mean '{match}'? (yes/no): ")
            if choice.casefold() in ['yes', 'y']:
                return options.index(match)
            else:
                match = sbert_match(request, options)
                if match:
                    choice = input(f"Did you mean '{match}'? (yes/no): ")
                    if choice.casefold() in ['yes', 'y']:
                        return options.index(match)
                else:
                    print("No exact match found. Here are the possible requests:")
                    for request in options:
                        print(f"- {request}")
        else:
            match = sbert_match(request, options)
            if match:
                choice = input(f"Did you mean '{match}'? (yes/no): ")
                if choice.casefold() in ['yes', 'y']:
                    return options.index(match)
            else:
                print("No exact match found. Here are the possible requests:")
                for request in options:
                    print(f"- {request}")


def prompt_input_request(options: list[str]) -> str:
    """
    Display the possible options to the user with the following format:
    1) Individual 1
    2) Individual 2
    ...
    And request the user to choose one of the options.
    Args:
        options (list[str]): list of individuals that can be requested
    Returns:
         output (int): request
    """
    # Display the options to the user
    print(f"\nThe following parameters can be computed:")

    # Display the available options: possible input combination + their corresponding workflow
    for index, option in enumerate(options, start=1):
        print(f"\t {index}. {option}")

    while True:
        output = input("Type your request number: ")
        if int(output) <= len(options):
            return int(output)-1
        else:
            print(f"Only {len(options)} options are available. Your request '{output}' can't be processed. Please select a "
                  f"valid option.")


def display_options(request: str, options: list[str], options_dict: dict[str, dict[str, list[list[str]]]]) -> None:
    """
    Display the options to the user with the following format:
    1) Method_req (=Method that can compute request):
        1. Input combination: input1, input2, ... (workflow 1)
            [Workflow steps]
            - input1 -> method -> output1, output2, ...
            - input2 -> method -> output1, output2, ...
        2. Input combination: input1, input2, ... (workflow 2)
            - input1 -> method -> output1, output2, ...
            - input2 -> method -> output1, output2, ...
    Args:
        request (str): request from the user
        options (list[str]): list of methods that can compute request
        options_dict (dict[str, dict[str, list[list[str]]]]): dict of methods that can compute request with their
        corresponding workflow options
    Returns:
        None: display the options in terminal
    """
    # Display the options to the user
    print(f"\nThe following method can compute {request}:")

    # Display the available options: possible input combination + their corresponding workflow
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}:")
        print(f'\t {len(options_dict[option].keys())} possible workflow(s):')
        for index_input, option_input in enumerate(options_dict[option].keys(), start=1):
            print(f"\t- {index_input}. Input: {option_input}")
            workflow = options_dict[option][option_input]
            for method in workflow:
                input_txt = ''
                for i, item in enumerate(method[0].split(', ')):
                    # Display necessary inputs in bold
                    if item in option_input.split(', '):
                        if i == 0:
                            input_txt += '\033[1m' + item + '\033[0m'
                        else:
                            input_txt += ', ' + '\033[1m' + item + '\033[0m'
                    else:
                        if i == 0:
                            input_txt += item
                        else:
                            input_txt += ', ' + item
                print(f"\t\t- {input_txt} -> {method[1]} -> {method[2]}")


def choose_options(options: list[str], dict_methods: dict[str, dict[str, list[list[str]]]]) -> tuple[int, int]:
    """
    Prompt user for method and workflow choice.
    Args:
        options: list of methods that can compute request
        dict_methods: dict of methods that can compute request with their
        corresponding workflow options
    Returns:
        choice_method (int): index of the chosen method
        choice_input (int): index of the chosen workflow
    """
    # Get user method choice
    while True:
        try:
            choice_method = int(input("Enter the method of your choice (number): "))
            if 1 <= choice_method <= len(options):
                break
            else:
                print("Invalid method choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get user workflow choice
    while True:
        try:
            choice_input = int(input("Enter the workflow of your choice (number): "))
            if 1 <= choice_input <= len(list(dict_methods[options[choice_method - 1]].keys())):
                break
            else:
                print("Invalid inputs choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return choice_method, choice_input


def post_process_sparql_results(sparql_results: list[list[str]]) -> list[list[str, list[str], list[str]]]:
    """
    Post-processing of sparql queries. Allow to store inputs and outputs concatenated by sparql into lists for future
    iteration over them.
    Args:
        sparql_results (list(list[str]): sparql queries with format
        [['method1', 'input1, input2', 'output1'], ['method2', 'input3', 'output2, output3']]
    Returns:
        post_processed_queries (list(list[str, list[str], list[str]])): post processed queries with format
        [['method1', ['input1','input2'], ['output1']], ['method2', ['input3'], ['output2' , 'output3']]]
    """

    post_processed_queries = copy.deepcopy(sparql_results)

    # Store inputs and outputs as list of strings
    for sublist in post_processed_queries:
        for i in range(1, 3):
            try:
                sublist[i] = sublist[i].split(', ')
            except AttributeError:
                sublist[i] = [sublist[i]]

        inputs = sublist[1]
        outputs = sublist[2]

        # Verify inputs and outputs are unique (could be remove if owlready2 support distinct in group_concat)
        sublist[1] = check_uniqueness_sublist(inputs)
        sublist[2] = check_uniqueness_sublist(outputs)

    return post_processed_queries


def list_to_string(list_of_strings: list[str]) -> str:
    """
    Transform a list of strings to one string with elements separated by a comma
    Args:
        list_of_strings (list[str]): list of strings
    Returns: one string with elements from the list separated by a comma
    """

    return ', '.join(list_of_strings)


def find_sublist_containing_item(list_of_lists: list[list[str]], item: str) -> list[list[str]]:
    """
    Check if an item is present in a list of lists and return the lists containing this item.
    TODO: only work for single item but output could be more than one (not in the current implementation but should be one day)
    Args:
        list_of_lists (list[list[str]]): list of list of strings
        item (str): item to check the presence of
    Returns:
        List of sublists that contain the input item
    """

    list_of_sublists = []
    for sublist in list_of_lists:
        if item in sublist:
            list_of_sublists.append(sublist)
    return list_of_sublists


def check_uniqueness_sublist(list_combination: list[str]) -> list[str]:
    """
    Check if every sublist of a list contains unique item. Return list of sublists with unique items.
    Args:
        list_combination (list[str]): list of strings
    Returns:
        List of unique strings in the same order as the input list
    """
    # If every item is unique, return the list
    if len(list_combination) == len(set(list_combination)):
        return list_combination
    # Else, remove duplicates
    else:
        unique_list = []
        [unique_list.append(item) for item in list_combination if item not in unique_list]
        return unique_list


def find_steps_cwl(ontology: Ontology, workflow: list[list[str]], path_to_cwl_folder: str) -> list[str]:
    """
    Query ontology to retrieve cwl file for the corresponding method through 'isDefinedBy' property.
    Args:
        ontology: an owl ontology
        workflow (list[list[str]]): list of [method, input, output]
    Returns:
        List of ['path to cwl file']
    """
    workflow_steps = []
    # Loop over the steps of the workflow
    for step in workflow:
        method_cwl = find_method_cwl(ontology, step[1])  # step[1] is the method name
        method_cwl_path = Path(os.path.join(path_to_cwl_folder, method_cwl[0][0]))
        workflow_steps.append(method_cwl_path)
    return workflow_steps


def retrieve_steps_information(wf: WorkflowGenerator, workflow_steps: list[str]) -> (dict[str, list[str]], dict[str, list[str]]):
    """
    Retrieve inputs and outputs for each step of the workflow.
    Args:
        wf (WorkflowGenerator): workflow object
        workflow_steps (list[str]): list of paths to cwl files
    Returns:
        steps_inputs (dict[str,list[str]]): dict of inputs (values) for each step (key). Inputs are in the form of 'input_name: input_type'.
        steps_outputs (dict[str,list[str]]): dict of outputs (values) for each step (key). Outputs are in the form of 'output_name: output_type'.
    """
    # Initialize dicts
    steps_inputs = {}
    steps_outputs = {}
    # Loop over the step (as path to cwl files)
    for step_path in workflow_steps:
        wf.load(step_file=step_path)  # load step into workflow object steps library
        # Retrieve step inputs and outputs from the library and store them in their corresponding dict.
        step_name = os.path.splitext(os.path.basename(step_path))[0]
        step_outputs_dict = wf.steps_library.get_step(step_name).output_types
        steps_outputs[step_name] = [f"{key}: '{value}'" for key, value in step_outputs_dict.items()]
        step_inputs_optional_dict = wf.steps_library.get_step(step_name).optional_input_types
        step_inputs_dict = wf.steps_library.get_step(step_name).input_types
        steps_inputs[step_name] = [f"{key}: '{value}'" for key, value in step_inputs_dict.items()] + [
            f"{key}: '{value}'" for key, value in step_inputs_optional_dict.items()]

    return steps_inputs, steps_outputs


def simplify_wf_inputs(wf_inputs: dict[str, list[str]], links: dict[str, list[(str, str)]], inputs_match: dict[str, dict[str, str]]) -> None:
    """
    Remove inputs that are linked to previous outputs from the workflow inputs.
    Args:
        wf_inputs (dict[str, list[str]]): dict of inputs (values) for each step (key). Inputs are in the form of 'input_name: input_type'.
        links (dict[str, list[(str, str)]]): dict of links between inputs and outputs. Key is the link name and value is a list of tuples (output, input). Inputs and outputs are in the form of 'input/output_name: input/output_type'.
        inputs_match (dict[str, dict[str, str]]): dict of name matches for inputs. Key is the step name and value is a dict of original input names (key) and corresponding name after linking (value).
    Returns:
        wf_inputs and inputs_match are modified in place.
    """
    for key in links.keys():
        step = key.split('-')[1]  # retrieve step name n+1 (the one with the input link to previous output)
        for value in links[key]:
            wf_inputs[step].remove(value[1])  # remove the input link to previous output from workflow inputs
            inputs_match[step][value[1].split(':', 1)[0]] = key.split('-')[0] + '/' + value[0].split(':', 1)[0]  # update inputs name in inputs_match


def modify_duplicate_name(duplicate_inp: str, wf_inputs: dict[str, list[str]], inputs_match: dict[str, dict[str, str]],
                          step_1: str, step_2: str) -> None:
    """
        Modify duplicate inputs name by indexing them with their corresponding step name and update workflow inputs names and inputs_match names.
    Args:
        duplicate_inp (str): duplicate input name with format 'input_name: input_type'
        wf_inputs (dict[str, list[str]]): dict of inputs (values) for each step (key). Inputs are in the form of 'input_name: input_type'.
        inputs_match (dict[str, dict[str, str]]): dict of name matches for inputs. Key is the step name and value is a dict of original input names (key) and corresponding name after linking (value).
        step_1 (str): step name n
        step_2 (str): step name n+1
    Returns:
         wf_inputs and inputs_match modified in place.
    """
    new_inp_name_step_1 = duplicate_inp.split(':', 1)[0] + f'_{step_1}:' + duplicate_inp.split(':', 1)[1]
    wf_inputs[step_1] = [new_inp_name_step_1 if item == duplicate_inp else item for item in
                         wf_inputs.get(step_1)]
    new_inp_name_step_2 = duplicate_inp.split(':', 1)[0] + f'_{step_2}:' + duplicate_inp.split(':', 1)[1]
    wf_inputs[step_2] = [new_inp_name_step_2 if item == duplicate_inp else item for item in
                         wf_inputs.get(step_2)]
    inputs_match[step_1][duplicate_inp.split(':', 1)[0]] = new_inp_name_step_1.split(':', 1)[0]
    inputs_match[step_2][duplicate_inp.split(':', 1)[0]] = new_inp_name_step_2.split(':', 1)[0]




