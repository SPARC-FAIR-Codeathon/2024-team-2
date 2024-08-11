import owlready2 as owl
import os
import json
import argparse

from owlready2.namespace import Ontology
from owlready2 import Thing as Individual


class KG:

    def __init__(self, ontology, tool_library):
        self._ontology = ontology
        self._tool_library = tool_library

    def create(self, save_path):
        # Get ontology
        ontology = owl.get_ontology(self._ontology).load()

        # Retrieve json files with tool description
        tools_descriptions = [os.path.join(self._tool_library, f) for f in os.listdir(self._tool_library) if
                              f.endswith('.json')]

        for description in tools_descriptions:
            # Retrieve individuals already in KG
            individuals = list(ontology.individuals())
            individual_names = [str(indiv_onto).removeprefix(self._ontology[:-3]) for indiv_onto in individuals]

            # Read description
            with open(description, 'r') as read_description:
                data = json.load(read_description)
                keys = list(data.keys())
                for key in keys:
                    if key == 'Input':
                        # Create list of input individuals
                        input_individuals = self._populate_ontology(ontology, individual_names, individuals, data[key])

                    elif key == 'Output':
                        # Create list of output individuals
                        output_individuals = self._populate_ontology(ontology, individual_names, individuals, data[key])

                    elif key == 'Operation':
                        method_name = data[key]
                        method = ontology.operation_0004(method_name)

                # Link inputs and outputs to method
                method.has_input = input_individuals
                method.has_output = output_individuals

                # Add description, label and cwl file name
                # method.comment = data['comment'] Maybe for later for NLP
                method.label = method_name
                method.isDefinedBy = data['cwl']

        # Save ontology
        ontology.save(file=save_path)

    def _populate_ontology(self, ontology: Ontology, individual_names: list[str], individuals: list[Individual],
                           class_data: list[dict]) -> list[Individual]:
        """
        Create a list of individuals for a specific key (either input or output) for the tool and add them in the knowledge
        graph if not existing.
        Args:
            ontology (Ontology): an owl ontology
            individual_names (list[str]): list of individual names existing in the knowledge graph
            individuals (list[Individual]):  list of individuals existing in the knowledge graph
            class_data (list[dict]): tool description stored in a dict format
        Returns:
            individuals_list (list[Individual]): list of individuals for the class specified in class_data
        """
        individuals_list = []
        for i in range(len(class_data)):
            # If individual already in KG add to list, else create and add to list
            if list(class_data[i].keys())[0] in individual_names:
                id_indiv = individual_names.index(list(class_data[i].keys())[0])
                tmp_individual = individuals[id_indiv]
            else:
                tmp_individual = ontology.data_0006(list(class_data[i].keys())[0])
                tmp_individual.label = list(class_data[i].keys())[0]
            individuals_list.append(tmp_individual)
        return individuals_list
