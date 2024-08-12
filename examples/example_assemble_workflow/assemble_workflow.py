import argparse

from sparc_assemble.core.assembler.assembler import Assembler


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--kg_path", type=str, help='Path to Knowledge Graph',
                        default=r"../../resources/dummy_kg.owl")
    args = parser.parse_args()

    assembler = Assembler(args.kg_path)
    assembler.run()
