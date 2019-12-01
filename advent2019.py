import argparse
import importlib
import os
import pathlib
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("days", nargs="*")
    parser.add_argument("--data-file")
    args = parser.parse_args()

    script_dir = pathlib.Path(__file__).parent
    solution_filenames = (f for f in os.listdir(script_dir) if "sol" in f)
    solved_days = sorted(f[3:-3] for f in solution_filenames)
    days = args.days or solved_days

    for day_arg in days:
        day = f"{int(day_arg):02}"
        if args.data_file is not None:
            data_filename = args.data_file
        else:
            data_filename = f"data/{day}.txt"
        with open(data_filename, "r") as data_file:
            data = data_file.read()

        solution_module = importlib.import_module(f"sol{day}")
        result = solution_module.run(data)

        print(f"Day {day} answer with data file {data_filename}:")
        print(result)


if __name__ == "__main__":
    sys.exit(main())
