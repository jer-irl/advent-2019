import argparse
import importlib
import itertools
import os
import pathlib
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzles", nargs="*")
    parser.add_argument("--data-file")
    args = parser.parse_args()

    script_dir = pathlib.Path(__file__).parent
    solution_filenames = (f for f in os.listdir(script_dir) if "sol" in f)
    solved_days = sorted(f[3:-3] for f in solution_filenames)
    puzzles = args.puzzles or solved_days

    for puzzle_arg in puzzles:
        puzzle = f"{int(puzzle_arg[:-1]):02}{puzzle_arg[-1]}"
        if args.data_file is not None:
            data_filename = args.data_file
        else:
            data_filename = f"data/{puzzle}.txt"
        with open(data_filename, "r") as data_file:
            data = data_file.read()

        solution_module = importlib.import_module(f"sol{puzzle}")
        result = solution_module.run(data)

        print(f"Puzzle {puzzle} answer with data file {data_filename}:")
        print(result)


if __name__ == "__main__":
    sys.exit(main())
