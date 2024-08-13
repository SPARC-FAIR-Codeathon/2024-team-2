import argparse

from sparc_assemble import Assembler


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--kg_path", type=str, help='Path to Knowledge Graph',
                        default=r"resources/kg_example_1.owl")
    parser.add_argument("--tools_path", type=str, help='Path to cwl tools folder',
                        default=None)
    args = parser.parse_args()

    assembler = Assembler(args.kg_path)
    assembler.run(args.tools_path)
