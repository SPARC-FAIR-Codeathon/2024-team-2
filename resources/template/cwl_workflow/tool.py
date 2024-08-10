import argparse

def main():
    print("Importing data into SDS")
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--input_folder", required=True, help="")
    parser.add_argument("--output_folder", required=True, help="")
    args = parser.parse_args()


if __name__ == "__main__":
    main()
