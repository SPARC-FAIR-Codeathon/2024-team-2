import argparse

from sparc_assemble.core.kg import KG

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--save_kg_path", type=str, help='Path to save KG', default=r"./kg_biomodels_model.owl")

    args = parser.parse_args()

    import biomodels
    # Retrieve metadata for the specified model using its unique identifier
    metadata = biomodels.get_metadata("BIOMD0000000012")
    # Download the model file in XML format based on the model ID and URL, and store it locally
    metadata_file = biomodels.get_file("BIOMD0000000012_url.xml", model_id="BIOMD12")
    # Convert the file's path to a string and get the directory path where the file is stored
    metadata_file_cache_path = str(metadata_file.parent)

    import simplesbml
    # Construct the full path to the downloaded model file by combining the directory path and file name
    model_path = metadata_file_cache_path + '/BIOMD0000000012_url.xml'
    # Load the SBML model from the specified file path using simplesbml
    model = simplesbml.loadSBMLFile(model_path)
    # Retrieve the name of the model
    model_name = model.model.name
    # Extract all species (inputs) from the model and store them in a list
    species = model.model.species.all_elements
    # Extract all reactions (outputs) from the model and store them in a list
    reactions = model.model.reactions.all_elements

    species_dict = {}
    inputs = []
    # Iterate over the species objects
    for specie in species:
        # Create a string representation for the key using the species ID and name
        key = f'Species {specie.id} "{specie.name}"'

        # Assign a nested dictionary as the value with the desired attributes
        species_dict = {
            key:{
            "type": specie.species_type,
            }
        }
        inputs.append(species_dict)

    reactions_dict = {}
    outputs = []
    # Iterate over the reactions objects
    for reaction in reactions:
        # Create a string representation for the key using the species ID and name
        key = f'Reactions {reaction.id} "{reaction.name}"'

        # Assign a nested dictionary as the value with the desired attributes
        reactions_dict = {
            key:{
            "type": "",
            }
        }
        outputs.append(reactions_dict)

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
