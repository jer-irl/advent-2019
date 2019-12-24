import enum
from typing import List, Tuple, Dict

from . import IntCodeComputer, OPCODES, StepResult


class TileColor(enum.IntEnum):
    BLACK = 0
    WHITE = 1


class TurnDirection(enum.IntEnum):
    LEFT = 0
    RIGHT = 1


class Bearing:
    _UP = (0, 1)
    _RIGHT = (1, 0)
    _DOWN = (0, -1)
    _LEFT = (-1, 0)
    _BEARINGS = [_UP, _RIGHT, _DOWN, _LEFT]

    def __init__(self):
        self.bearing = 0

    def get_dxdy(self):
        return self._BEARINGS[self.bearing]

    def turn(self, turn_direction: TurnDirection):
        if turn_direction == TurnDirection.LEFT:
            self.bearing = (self.bearing - 1) % len(self._BEARINGS)
        elif turn_direction == TurnDirection.RIGHT:
            self.bearing = (self.bearing + 1) % len(self._BEARINGS)


class HaltException(Exception):
    pass


def run_until_output(brain: IntCodeComputer) -> int:
    while len(brain.context.output) < 1:
        step_result = brain.run_step()
        if step_result == StepResult.HALT:
            raise HaltException()
        elif step_result == StepResult.INPUT:
            raise RuntimeError()

    assert len(brain.context.output) == 1
    return brain.context.output.pop(0)


def input_color(board: Dict[Tuple[int, int], TileColor], brain: IntCodeComputer, robot_loc: Tuple[int, int]):
    if robot_loc in board:
        color = board[robot_loc]
    else:
        color = TileColor.BLACK
    brain.context.input.append(color)


def paint(board: Dict[Tuple[int, int], TileColor], brain: IntCodeComputer, robot_loc: Tuple[int, int]):
    color = run_until_output(brain)
    board[robot_loc] = TileColor(color)


def turn(brain: IntCodeComputer, robot_bearing: Bearing):
    turn_dir = run_until_output(brain)
    robot_bearing.turn(TurnDirection(turn_dir))


def move_one(robot_loc: Tuple[int, int], robot_bearing: Bearing) -> Tuple[int, int]:
    x, y = robot_loc
    dx, dy = robot_bearing.get_dxdy()
    return x + dx, y + dy


def run_step(
        board: Dict[Tuple[int, int], TileColor],
        brain: IntCodeComputer,
        robot_loc: Tuple[int, int],
        robot_bearing: Bearing
) -> Tuple[int, int]:
    input_color(board, brain, robot_loc)
    paint(board, brain, robot_loc)
    turn(brain, robot_bearing)
    return move_one(robot_loc, robot_bearing)


def run_until_halt(board: Dict[Tuple[int, int], TileColor], brain: IntCodeComputer):
    bearing = Bearing()

    # Exception flow-control is bad, this wouldn't fly in production
    try:
        location = (0, 0)
        while True:
            location = run_step(board, brain, location, bearing)
    except HaltException:
        pass


def run(data):
    program = [int(x) for x in data.split(",")]
    brain = IntCodeComputer(program, OPCODES)
    board = dict()
    run_until_halt(board, brain)
    return len(board)
