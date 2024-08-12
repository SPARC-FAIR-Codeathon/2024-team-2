import argparse

from sparc_assemble.core.kg import KG

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--save_kg_path", type=str, help='Path to save KG', default=r"./kg_biomodels_model.owl")
    args = parser.parse_args()

    inputs = []
    outputs = []
    model_name = ""
    model_path = ""

    # initialising KG from default ontology "EDAM"
    kg = KG()
    # kg.save(save_path=args.save_kg_path)

    # # initialising KG from a give ontology
    # kg = KG(ontology_file=args.save_kg_path)

    # adding tools to KG
    kg.add_biomodels_model(inputs, outputs, model_name, model_path)

    # listing tools in KG
    kg.list()

    kg.save(save_path=args.save_kg_path)
