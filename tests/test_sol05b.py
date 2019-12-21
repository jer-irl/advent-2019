from typing import List

from sols.sol05b import IntCodeComputer, OPCODES


def run_with_input(program: List[int], input_values: List[int]):
    computer = IntCodeComputer(program.copy(), OPCODES)
    computer.context.input = input_values
    while not computer.run_step():
        pass
    assert len(computer.context.output) == 1
    return computer.context.output[0]


def test_run_program():
    program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    assert run_with_input(program, [7]) == 0
    assert run_with_input(program, [8]) == 1
    assert run_with_input(program, [9]) == 0

    program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    assert run_with_input(program, [7]) == 1
    assert run_with_input(program, [8]) == 0
    assert run_with_input(program, [9]) == 0

    program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    assert run_with_input(program, [7]) == 0
    assert run_with_input(program, [8]) == 1
    assert run_with_input(program, [9]) == 0

    program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    assert run_with_input(program, [7]) == 1
    assert run_with_input(program, [8]) == 0
    assert run_with_input(program, [9]) == 0

    program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    assert run_with_input(program, [-1]) == 1
    assert run_with_input(program, [0]) == 0
    assert run_with_input(program, [1]) == 1

    program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    assert run_with_input(program, [-1]) == 1
    assert run_with_input(program, [0]) == 0
    assert run_with_input(program, [1]) == 1

    program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
               1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
               999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
    assert run_with_input(program, [6]) == 999
    assert run_with_input(program, [7]) == 999
    assert run_with_input(program, [8]) == 1000
    assert run_with_input(program, [9]) == 1001
    assert run_with_input(program, [10]) == 1001
