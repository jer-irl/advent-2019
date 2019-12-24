from typing import Dict, Tuple

from sols.sol11a import run_until_halt, IntCodeComputer, OPCODES, TileColor


def board_string(board: Dict[Tuple[int, int], TileColor]):
    max_y = max(y for (x, y) in board.keys())
    min_y = min(y for (x, y) in board.keys())
    max_x = max(x for (x, y) in board.keys())
    min_x = min(x for (x, y) in board.keys())

    result = ""
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            color = board[(x, y)] if (x, y) in board else TileColor.BLACK
            if color == TileColor.BLACK:
                result += " "
            elif color == TileColor.WHITE:
                result += "X"
            else:
                raise RuntimeError()
        result += "\n"

    return result


def run(data):
    program = [int(x) for x in data.split(",")]
    brain = IntCodeComputer(program, OPCODES)
    board = dict()
    board[(0, 0)] = TileColor.WHITE
    run_until_halt(board, brain)
    return board_string(board)
