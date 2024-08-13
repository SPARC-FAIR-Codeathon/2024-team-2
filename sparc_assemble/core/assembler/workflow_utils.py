from owlready2.namespace import Ontology
from sparc_assemble.core.assembler.workflow import WorkflowGenerator
from scriptcwl.reference import Reference
from sparc_assemble.core.assembler.assemble_utils import *


def find_duplicate_inputs_name(wf_inputs: dict[str, list[str]]) -> dict[str, list[str]]:
    """
    Find inputs with same name between steps.
    Args:
        wf_inputs (dict[str, list[str]]): dict of inputs (values) for each step (key). Inputs are in the form of 'input_name: input_type'.
    Returns:
        dict of inputs with same name between steps. Key is the link name (step_n-step_n+1) and value is a list of inputs with same name between these steps.
    """
    list_inputs = list(wf_inputs.values())
    list_steps = list(wf_inputs.keys())
    duplicate_name_dict = {}
    for i in range(len(list_inputs) - 1):
        # Convert the lists to sets for efficient intersection
        set1 = set(list_inputs[i])
        tmp_list = list_inputs[i + 1:]
        for sublist in tmp_list:
            set2 = set(sublist)

            # Find the common elements
            common = set1.intersection(set2)

            # Convert the set back to a list if needed
            duplicate_name_dict[f'{list_steps[i]}-{list_steps[i + 1]}'] = list(common)

    return duplicate_name_dict


def modify_duplicate_inputs(duplicate_inputs: dict[str, list[str]], wf_inputs: dict[str, list[str]], inputs_match: dict[str, dict[str, str]]) -> None:
    """
    Modify duplicate inputs name according to user choices.
    Args:
        duplicate_inputs (dict[str, list[str]]): dict of inputs with same name between steps. Key is the link name (step_n-step_n+1) and value is a list of inputs with same name between these steps.
        wf_inputs (dict[str, list[str]]): dict of inputs (values) for each step (key). Inputs are in the form of 'input_name: input_type'.
        inputs_match (dict[str, dict[str, str]]): dict of name matches for inputs. Key is the step name and value is a dict of original input names (key) and corresponding name after linking (value).
    Returns:
        wf_inputs and inputs_match modified according to user choices.
    """
    # Count total number of duplicate inputs
    total_duplicate = sum(len(sublist) for sublist in duplicate_inputs.values())
    print(
        f'{total_duplicate} inputs are duplicated (same name and same type). \n Please select the ones that represent '
        f'the same input [y]. Otherwise [n], they will be indexed according to their step.')
    # Loop over steps with duplicate inputs
    for key in list(duplicate_inputs.keys()):
        # Loop over duplicate inputs between the 2 current steps
        for duplicate_inp in duplicate_inputs[key]:
            print(f'Input: {duplicate_inp} is duplicated between step {key.split("-")[0]} and {key.split("-")[1]}.')
            choice = str(input("Does it represent the same input for these two steps? "))
            # If duplicate inputs name represent the same input, remove the duplicated one from workflow inputs
            if choice.casefold() in ['yes', 'y']:
                step_2 = key.split('-')[1]
                wf_inputs[step_2].remove(duplicate_inp)
            # Else, modify their name by indexing them with their corresponding step name and update workflow inputs names
            else:
                step_1 = key.split('-')[0]
                step_2 = key.split('-')[1]
                modify_duplicate_name(duplicate_inp, wf_inputs, inputs_match, step_1, step_2)


def link_steps(outputs: dict[str, list[str]], inputs: dict[str, list[str]]) -> dict[str, list[str]]:
    """
    Link outputs from previous steps to inputs of the next step.
    Args:
        outputs (dict[str, list[str]]): dict of outputs (values) for each step (key). Outputs are in the form of 'output_name: output_type'.
        inputs (dict[str, list[str]]): dict of inputs (values) for each step (key). Inputs are in the form of 'input_name: input_type'.
    Returns:
        Dict of linked inputs and outputs for each pair of step linked. Format: dict{step_n-step_n+1: [("output_name: 'output_type'", "input_name: 'input_type'")]} for all linked steps
    """
    steps_name = list(inputs.keys())
    # Initialize lists and linked dict
    link_dict = {}
    # Loop over steps
    for index, method in enumerate(steps_name):
        # If first step, only store inputs as there is no previous step/outputs
        if index == 0:
            # Print current step and its inputs
            print(f'Step {index + 1} ({steps_name[index]}) inputs: {inputs[method]} \n')
        else:
            # Print current step and its inputs
            print(f'Step {index + 1} ({steps_name[index]}) inputs: {inputs[method]}')
            inputs_dict = {key.strip(): value.strip(" '") for item in inputs[method] for key, value in
                           [item.split(':', 1)]}  # dict{input_name: input_type} for current step
            # Retrieve outputs available from all previous steps: dict{step_name: ['output_name: output_type']}
            outputs_available = {prev_method: outputs[prev_method] for prev_method in steps_name[:index]}
            outputs_dict = {key: value for d in [
                {key.strip(): value.strip(" '") for item in outputs_available_list for key, value in
                 [item.split(':', 1)]} for outputs_available_list in outputs_available.values()] for key, value in
                            d.items()} # dict{output_name: output_type} for all previous steps
            print(f'Outputs available at this step: {outputs_available} \n')
            choice = str(input("Does any input of current step need to be linked to a previous output (yes/no): "))
            while choice.casefold() in ['yes', 'y']:
                input_to_link = str(input('\nInput name: ')).casefold()
                output_to_link = str(input('Output_name: ')).casefold()
                # Check if input and output provided are in available inputs/outputs
                if input_to_link in inputs_dict.keys() and output_to_link in outputs_dict.keys():
                    # Check type correspondence
                    if inputs_dict[input_to_link] == outputs_dict[output_to_link]:
                        key_steps = steps_name[index - 1] + '-' + steps_name[index]
                        # If link key already in dict, add new value
                        if key_steps in link_dict.keys():
                            value_steps = ('"' + output_to_link + ': ' + "'" + outputs_dict[output_to_link] + "'" + '"',
                                           '"' + input_to_link + ': ' + "'" + inputs_dict[input_to_link] + "'" + '"') # ("output_name: 'output_type'", "input_name: 'input_type'")
                            if value_steps in link_dict[key_steps]:
                                print('The link already exists.')
                            else:
                                link_dict[key_steps].append(value_steps)
                        # Else, create new link key and value
                        else:
                            value_steps = [(output_to_link + ': ' + "'" + outputs_dict[output_to_link] + "'",
                                            input_to_link + ': ' + "'" + inputs_dict[input_to_link] + "'")]
                            link_dict[key_steps] = value_steps
                        print('Done.')
                        choice = str(input('Is there another link to create? '))
                    else:
                        print('Input and output provided are not the same type.')
                        choice = str(input('Try again? '))
                else:
                    print('Input or output provided not in available inputs/outputs.')
                    choice = str(input('Try again? '))
    return link_dict # dict{step_n-step_n+1: [("output_name: 'output_type'", "input_name: 'input_type'")]} for all linked steps


def add_workflow_inputs(wf: WorkflowGenerator, wf_inputs: dict[str, list[str]]) -> dict[str, str]:
    """
    Add workflow inputs to the workflow object and store the final version of the workflow inputs in a dict.
    Args:
        wf (WorkflowGenerator): workflow object
        wf_inputs (dict[str, list[str]]): dict of inputs (values) for each step (key). Inputs are in the form of 'input_name: input_type'.
    Returns:
        global_inputs (dict[str, str]): dict of inputs for the workflow. Inputs are in the form of 'input_name: input_type'.
    """
    steps_names = wf_inputs.keys()
    global_inputs = {}
    # Loop over steps
    for name in steps_names:
        # Loop over inputs for each step
        for i in range(len(wf_inputs[name])):
            inp = {wf_inputs[name][i].split(':')[0]: wf_inputs[name][i].split(':', 1)[1][2:-1]} # dict{name:type}
            if '{' in wf_inputs[name][i].split(':', 1)[1][2:-1]: #handle special type such as File or Directory
                inp[wf_inputs[name][i].split(':')[0]] = eval(wf_inputs[name][i].split(':', 1)[1][2:-1])
            # Add input to workflow object
            wf.add_input(**inp) #TODO: this function can output reference for each input
            # Add input: dict{name:type} to global inputs dict
            global_inputs.update(inp)
    return global_inputs


def add_steps(wf: WorkflowGenerator, inputs_match: dict[str, dict[str, str]]) -> dict[str, list[Reference]]:
    """
    Add steps to the workflow object and store the final version of the workflow outputs in a dict.
    Args:
        wf (WorkflowGenerator): workflow object
        inputs_match (dict[str, dict[str, str]]): dict of name matches for inputs. Key is the step name and value is a dict of original input names (key) and corresponding name after linking (value).

    Returns:
        outputs_references (dict[str, list[Reference]]): dict of outputs for the workflow. Outputs are Reference.
    """
    outputs_references = {}
    # Loop over step
    for step, step_inputs in inputs_match.items():
        step_inputs_reference = {}
        # Loop over inputs for each step
        for key, value in step_inputs.items():
            if '/' in value:  # handle input linked to previous output
                step_inputs_reference[key] = Reference(step_name=value.split('/')[0], output_name=value.split('/')[1])
            else:
                step_inputs_reference[key] = Reference(input_name=value)
        make_step = wf.__getattr__(step, **step_inputs_reference)
        # Add make_step to outputs_references dict (make_step references the output)
        if step in outputs_references.keys():
            outputs_references[step].append(make_step())
        else:
            outputs_references[step] = [make_step()]
    return outputs_references


def add_workflow_outputs(wf: WorkflowGenerator, outputs_references: dict[str, list[Reference]]) -> None:
    """
    Add workflow outputs to the workflow object.
    Args:
        wf (WorkflowGenerator): workflow object
        outputs_references (dict[str, list[Reference]]): dict of outputs for the workflow. Outputs are Reference.
    Returns:
        None. wf is modified in place.
    """
    workflow_outputs = {str(value).split('/')[1]: value for key, values in outputs_references.items() for value in values} #TODO: handle same output name
    wf.add_outputs(**workflow_outputs)


def save_workflow(ontology: Ontology, workflow: list[list[str]], path_to_cwl_folder) -> tuple[dict, str]:
    """
    Create and save a CWL workflow from a list of steps (=workflow).
    Args:
        ontology (Ontology): an owl ontology
        workflow (list[list[str]]): list of [method, input, output] for each step of the workflow
    Returns:
        final_inputs (dict): dict of inputs for the workflow. Inputs are in the form of 'input_name: input_type'.
        workflow_name (str): name of the workflow
    """
    workflow_steps = find_steps_cwl(ontology, workflow, path_to_cwl_folder)
    # Create workflow object
    with WorkflowGenerator() as wf:
        # Load cwl file and store inputs and outputs in dicts with key = step name
        workflow_inputs, steps_outputs = retrieve_steps_information(wf, workflow_steps)
        # Link inputs and outputs between steps and store the links in a dict
        step_links = link_steps(steps_outputs, workflow_inputs)
        # Create dict of name matches for inputs. Key is the step name and value is a dict of original input names (key)
        # and corresponding name after linking (value).
        inputs_match = {key: {value.split(':', 1)[0]: value.split(':', 1)[0] for value in values} for key, values in workflow_inputs.items()}
        # Remove inputs link to previous outputs from workflow inputs and update inputs_match
        simplify_wf_inputs(workflow_inputs, step_links, inputs_match)  # TODO: something will go wrong for input_match if partially simplified and then change name
        # Find inputs with same name between steps and modify duplicate inputs name according to user choices
        duplicate_inputs_name = find_duplicate_inputs_name(workflow_inputs)
        if duplicate_inputs_name:
            modify_duplicate_inputs(duplicate_inputs_name, workflow_inputs, inputs_match)
        # Add workflow inputs, steps and outputs
        final_inputs = add_workflow_inputs(wf, workflow_inputs)
        out_ref = add_steps(wf, inputs_match)
        add_workflow_outputs(wf, out_ref)
        # Save workflow to a cwl file with name provided by user
        workflow_name = str(input('Workflow name: '))  # Get workflow name
        wf.save(f'workflows/{workflow_name}.cwl', mode='abs')  # TODO: remove hard coded path
    return final_inputs, workflow_name
