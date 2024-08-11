import argparse

from sparc_assemble.core.kg import KG

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--ontology", type=str, help='Path to ontology template',
                        default=r"../../resources/EDAM.owl")
    parser.add_argument("--tool_library", type=str, help='Path to tool library', default=r"../../resources/tools")
    parser.add_argument("--save_kg_path", type=str, help='Path to save KG', default=r"./KG.owl")

    args = parser.parse_args()

    kg = KG(ontology_file=args.ontology)
    kg.save(save_path=args.save_kg_path)

    kg = KG(ontology_file=args.save_kg_path)
    kg.add_tools(tool_library=args.tool_library)
    kg.list_added_tools()
    kg.save(save_path="args.tool_library")
