import argparse

from sparc_assemble.core.kg import KG

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--model_file", type=str, help='Path to model', default=r"../../resources/models/simulation.json")
    parser.add_argument("--save_kg_path", type=str, help='Path to save KG', default=r"./kg_sparc_model.owl")

    args = parser.parse_args()

    # initialising KG from default ontology "EDAM"
    kg = KG()
    # kg.save(save_path=args.save_kg_path)

    # # initialising KG from a give ontology
    # kg = KG(ontology_file=args.save_kg_path)

    # adding tools to KG
    kg.add_sparc_model(model_path=args.model_file)

    # listing tools in KG
    kg.list()

    kg.save(save_path=args.save_kg_path)
