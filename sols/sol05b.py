from typing import List

from . import IntCodeComputer, OPCODES


def run(data):
    program = [int(x) for x in data.split(",")]
    computer = IntCodeComputer(program, OPCODES)
    computer.context.input.append(5)
    while not computer.run_step():
        pass
    assert len(computer.context.output) == 1
    return computer.context.output[0]

