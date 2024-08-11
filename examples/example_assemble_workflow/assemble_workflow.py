import argparse

from sparc_assemble.core.assembler.assembler import Assembler


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--KG_path", type=str, help='Path to Knowledge Graph',
                        default=r"resources/KG.owl")
    parser.add_argument("--hpc", action='store_true', help='Set flag to run on hpc')
    args = parser.parse_args()

    assembler_instance = Assembler(args.KG_path, args.hpc)
    assembler_instance.run()