import argparse

from sparc_assemble.core.kg import KG

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--save_kg_path", type=str, help='Path to save KG', default=r"./kg_biomodels_model.owl")
    args = parser.parse_args()

    import biomodels
    metadata = biomodels.get_metadata("BIOMD0000000012")
    metadata_file = biomodels.get_file("BIOMD0000000012_url.xml", model_id="BIOMD12")
    metadata_file_cache_path = str(metadata_file.parent)

    import simplesbml
    model_path = metadata_file_cache_path + '/BIOMD0000000012_url.xml'
    model = simplesbml.loadSBMLFile(model_path)
    model_name = model.model.name
    inputs = list(model.model.species.all_elements)
    outputs = list(model.model.reactions.all_elements)

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
