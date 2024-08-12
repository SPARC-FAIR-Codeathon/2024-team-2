import argparse

from sparc_assemble.core.kg import KG

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--ontology", type=str, help='Path to ontology template',
                        default=r"../../resources/EDAM.owl")
    # parser.add_argument("--tool_library", type=str, help='Path to tool library', default=r"../../resources/tools")
    parser.add_argument("--tool_library", type=str, help='Path to tool library', default=r"./tools")
    parser.add_argument("--save_kg_path", type=str, help='Path to save KG', default=r"./tools_kg.owl")

    args = parser.parse_args()

    # initialising KG from default ontology "EDAM"
    kg = KG()
    kg.save(save_path=args.save_kg_path)

    # # initialising KG from a give ontology
    # kg = KG(ontology_file=args.save_kg_path)

    tool1 = {
            "Operation": "SDS_282",
            "comment": "From RNA sequences to BAM",
            "Input": [
                {"RNA sequences": {
                    "type": "file"
                }},
                {"Left ventricular mass": {
                    "type": ""
                }},
                {"PV loop": {
                    "type": ""
                }},
                {"E/A ratio": {
                    "type": ""
                }}
            ],
            "Output": [{
                "BAM": {
                    "type": "file"
                }
            }],
            "cwl": ""
        }

    tool2 = {
            "Operation": "ROCrate_525",
            "comment": "From BAM to outNpz",
            "Input": [
                {"BAM": {
                    "type": "file"
                }},
                {"Left ventricular mass": {
                    "type": ""
                }},
                {"PV loop": {
                    "type": ""
                }},
                {"E/A ratio": {
                    "type": ""
                }}
            ],
            "Output": [{
                "outNpz": {
                    "type": "file"
                }
            }],
            "cwl": "tools\\ChIP-Seq_workflow.cwl"
        }

    # Save both tool 1 and tool 2 dictionaries as json into a new folder in the current directory. Pass the folder path to this directory to the kg.add_tools() function.
    # adding tools to KG
    kg.add_tools(tool_library=args.tool_library)

    # listing tools in KG
    kg.list()

    kg.save(save_path=args.save_kg_path)
