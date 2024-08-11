import owlready2 as owl
import os
import json
import argparse

from owlready2.namespace import Ontology
from owlready2 import Thing as Individual


def populate_ontology(ontology: Ontology, individual_names: list[str], individuals: list[Individual],
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


def main(args):
    """
    Main function to populate the knowledge graph from tool description.
    """
    # Get ontology
    ontology = owl.get_ontology(args.ontology).load()

    # Retrieve json files with tool description
    tools_descriptions = [os.path.join(args.tool_library, f) for f in os.listdir(args.tool_library) if f.endswith('.json')]

    for description in tools_descriptions:
        # Retrieve individuals already in KG
        individuals = list(ontology.individuals())
        individual_names = [str(indiv_onto).removeprefix(args.ontology[:-3]) for indiv_onto in individuals]

        # Read description
        with open(description, 'r') as read_description:
            data = json.load(read_description)
            keys = list(data.keys())
            for key in keys:
                if key == 'Input':
                    # Create list of input individuals
                    input_individuals = populate_ontology(ontology, individual_names, individuals, data[key])

                elif key == 'Output':
                    # Create list of output individuals
                    output_individuals = populate_ontology(ontology, individual_names, individuals, data[key])

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
    ontology.save(file=args.save_KG_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--ontology", type=str, help='Path to ontology template',
                        default=r"../../resources/EDAM.owl")
    parser.add_argument("--tool_library", type=str, help='Path to tool library', default=r"../../resources/tools")
    parser.add_argument("--save_KG_path", type=str, help='Path to save KG', default=r"../../resources/KG.owl")

    args = parser.parse_args()

    main(args)
