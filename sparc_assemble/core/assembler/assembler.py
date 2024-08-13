from typing import Union

from sparc_assemble.core.assembler.sparql_queries import *
from sparc_assemble.core.assembler.workflow_utils import *

from owlready2.namespace import Ontology

class Assembler():
    """
    From a knowledge graph, prompt user for request, retrieve possible workflows, prompt user for workflow choice and
    create the corresponding workflow (cwl) and inputs (yaml) files.
    """
    def __init__(self, KG_path: str):
        self.KG_path = KG_path
        self.workflow_options_dict = None
        self.workflow = None

    def run(self, path_to_cwl_folder=None):
        """
        Main function of the program. Parse arguments, load ontology, display options to the user, prompt user for choice in
        a GUI or terminal. Run the chosen workflow.
        """
        # Retrieve ontology
        ontology = owl.get_ontology(self.KG_path).load()

        # Define request options
        request_options = [ind.name for ind in list(ontology.individuals()) if
                           ind.is_a[0] == ontology.data_0006 and ontology.is_output_of in ind.get_properties()]

        # Display request options and prompt for request
        selected_request = prompt_input_request_nlp(request_options)

        # Retrieve methods that answer the request and store all possible workflows in a global dict
        self._handle_request_choice(request_options[selected_request], ontology)

        # Prompt user for methods and workflows choice, save workflow and inputs values
        self._workflow_choice_and_save(workflow_options_dict, request_options[selected_request],
                                                              ontology, path_to_cwl_folder)



    def _handle_request_choice(self, selected_choice: str, ontology: Ontology) -> None:
        """
        Find methods that answer the request and store all possible workflows in a global dict.
        Args:
            selected_choice (str): request chosen by the user
            ontology (Ontology): an owl ontology
        Returns:
            None
        """
        methods = find_methods_from_request(ontology, selected_choice)
        global workflow_options_dict
        workflow_options_dict = self._create_options_workflow_dict(ontology, methods)

    def _create_options_workflow_dict(self, ontology: Ontology, methods: list[list[str]]) -> dict[
        str, dict[str, list[list[str]]]]:
        """
        Create a dict with keys (str)=method that answer the request and values (dict)= dict with keys (str)=input combination
        Args:
            ontology (Ontology): an owl ontology
            methods (list[list[str]]): list of ['method', 'input_1, input_2', 'output_1, output_2']
        Returns:
            res_dict (dict[dict[str, list[list[str]]]]): dict with keys (str)=method that answer the request and values (dict)= dict with keys
                                (str)=input combination and values (list(list[str]))=list representing the workflow used
        """
        res_dict = {}  # Initialize empty dict

        for method in methods:
            post_processed_queries = post_process_sparql_results([method])
            input_combination = [post_processed_queries[0][1]]
            input_txt = list_to_string(post_processed_queries[0][1])
            output_txt = list_to_string(post_processed_queries[0][2])
            method_txt = post_processed_queries[0][0]
            # Initialize dict with original input combination as key, and workflow as value
            workflows = {input_txt: [[input_txt, method_txt, output_txt]]}
            # Update dict with all possible input combinations and workflows
            self._retrieve_possible_workflows(ontology, post_processed_queries, input_combination, workflows)
            res_dict[post_processed_queries[0][0]] = workflows  # store workflows in dict with method as key

        return res_dict

    def _retrieve_possible_workflows(self, ontology: Ontology, queries_result: list[list[str, list[str], list[str]]],
                                    combination: list[str], workflows: dict) -> None:
        """
        Recursive function to retrieve all the possible input combinations and the workflow to get from the combination to
        the desired output.
        Args:
            ontology (Ontology): an owl ontology
            queries_result (list[list[str, list[str], list[str]]]): list(['method', ['input',...], ['output',...]]))
                                                                    post processed query result given an input
            combination (list(list[str]): list of list of strings corresponding to the possible input combination so far
            workflows (dict): dict with keys (str)=input combination and values (list(list[str]))=list representing the
                    workflow used with the corresponding input combination each sublist being ['input', 'method', 'output']
        Returns:
            None: modify combination and workflows on the fly
        """

        if queries_result:
            # Loop over the number of methods
            for i in range(len(queries_result)):
                # Loop over the number of inputs of each method
                for j in range(len(queries_result[i][1])):
                    current_input = queries_result[i][1][j]
                    # Find method(s) with output current_input
                    queries = find_inferred_inputs(ontology, current_input)
                    post_processed_queries = post_process_sparql_results(queries)
                    for query in post_processed_queries:
                        # Retrieve list where current_input existed and replace it with new input. Add it to combination.
                        list_containing_previous_input = find_sublist_containing_item(combination, current_input)
                        try:
                            for previous_inp in list_containing_previous_input:
                                index = previous_inp.index(current_input)
                                new_input = previous_inp[:index] + query[1] + previous_inp[index + 1:]
                                unique_new_input = check_uniqueness_sublist(new_input)
                                combination.append(unique_new_input)

                                # Add input combination to workflow dict with the corresponding methods to get to the
                                # desired output
                                input_txt = list_to_string(query[1])
                                output_txt = list_to_string(query[2])
                                workflows[list_to_string(unique_new_input)] = [
                                    [input_txt, query[0], output_txt]]  # query[0] = method
                                for previous_method in workflows[list_to_string(previous_inp)]:
                                    workflows[list_to_string(unique_new_input)].append(previous_method)
                        except Exception as e:
                            print(e)
                    self._retrieve_possible_workflows(ontology, post_processed_queries, combination, workflows)
            return ''
        # Stop condition: if no method found from the previous query
        else:
            return ''

    def _workflow_choice_and_save(self, options_dict: dict[str, dict[str, list[list[str]]]], request: str, ontology: Ontology,
                                  path_to_cwl_folder: str) -> Union[None | str, str]:
        """
        Prompt user to choose a method and an input combination plus inputs value of the corresponding combination.
        TODO: Only support choosing one method.
        Args:
            options_dict (dict[str, dict[str, list[list[str]]]]): key(str)=method that answer the request and values(dict)= dict
                        with keys(str)=input combination and values(list(list[str]))=list representing the workflow used
                        with the corresponding input combination each sublist being ['input', 'method', 'output']
            request (str): request typed by the user
            ontology (Ontology): an owl ontology
            interface (MainInterface): GUI interface
        Returns:
            chosen_option (str): method chosen
            inputs (list[str]): list of inputs values for the chosen inputs combination.
        """
        # Extract methods that answer the request
        options = list(options_dict.keys())

        display_options(request, options, options_dict)
        choice_method, choice_input = choose_options(options, options_dict)
        self._store_workflow_choice(choice_method, choice_input, options_dict, options)

        # Save workflow and inputs values respectively in Workflows (.cwl file) and Jobs (.yml file) folders
        if path_to_cwl_folder:
            wf_inputs, wf_name = save_workflow(ontology, self.workflow, path_to_cwl_folder)


    def _store_workflow_choice(self, choice_method: int, choice_input: int,
                              methods_dict: dict[str, dict[str, list[list[str]]]],
                              options: list[str]) -> None:
        """
        Retrieve the chosen workflow and store it in a global variable (workflow).
        Args:
            choice_method (int): index of the chosen method
            choice_input (int): index of the chosen input combination
            methods_dict (dict[str, dict[str, list[list[str]]]]): dict of methods that can compute request with their
            corresponding workflow options
            options (list[str]): list of methods that can compute request
        Returns:
            None: modify workflow on the fly
        """

        chosen_option = options[choice_method - 1]
        chosen_inputs = list(methods_dict[chosen_option].keys())[choice_input - 1]
        self.workflow = methods_dict[chosen_option][chosen_inputs]