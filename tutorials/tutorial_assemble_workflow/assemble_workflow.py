import argparse

from sparc_assemble import Assembler


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--kg_path", type=str, help='Path to Knowledge Graph',
                        default=r"../example_creating_knowledge_graph/kg.owl")
    parser.add_argument("--tools_path", type=str, help='Path to cwl tools folder',
                        default=r"../example_creating_knowledge_graph/tools")
    args = parser.parse_args()

    assembler = Assembler(args.kg_path)
    assembler.run(args.tools_path)
