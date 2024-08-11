import argparse

from sparc_assemble.core.kg import KG

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--ontology", type=str, help='Path to ontology template',
                        default=r"../../resources/EDAM.owl")
    parser.add_argument("--tool_library", type=str, help='Path to tool library', default=r"../../resources/tools")
    parser.add_argument("--save_kg_path", type=str, help='Path to save KG', default=r"../../resources/KG.owl")

    args = parser.parse_args()

    kg = KG(ontology=args.ontology, tool_library=args.tool_library)
    kg.create(save_path=args.save_kg_path)

