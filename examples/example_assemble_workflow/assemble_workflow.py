import argparse

from sparc_assemble.core.assembler.assembler import Assembler


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--KG_path", type=str, help='Path to Knowledge Graph',
                        default=r"../../resources/KG.owl")
    args = parser.parse_args()

    assembler_instance = Assembler(args.KG_path)
    assembler_instance.run()