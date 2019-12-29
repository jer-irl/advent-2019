from _collections import defaultdict
import enum

from sols import IntCodeComputer, StepResult, OPCODES


class TileType(enum.IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    HORIZONTAL_PADDLE = 3
    BALL = 4


def write_output(tiles, steps):
    for x, y, tile in steps:
        tiles[(x, y)] = tile


def run(data):
    program = [int(x) for x in data.split(",")]
    computer = IntCodeComputer(program, OPCODES)
    computation_result = computer.run()
    assert computation_result == StepResult.HALT

    tiles = defaultdict(int)
    steps = [tuple(computer.context.output[x:x + 3]) for x in range(0, len(computer.context.output), 3)]
    write_output(tiles, steps)
    return len([x for x in tiles.values() if x == TileType.BLOCK])
