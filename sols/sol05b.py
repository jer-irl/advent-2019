from typing import List

from sols.sol05a import (
    OpCode, IntCodeComputer, AddOpCode, MultiplyOpCode, HaltOpCode, InputOpCode, OutputOpCode, Parameter, StepResult
)


def _jump_if_true(computer: IntCodeComputer, parameters: List[Parameter]) -> StepResult:
    if computer.get_value(parameters[0]) != 0:
        computer.counter = computer.get_value(parameters[1])
    else:
        computer.counter += 3
    return StepResult.CONTINUE


JumpIfTrueOpCode = OpCode(5, 2, _jump_if_true)


def _jump_if_false(computer: IntCodeComputer, parameters: List[Parameter]) -> StepResult:
    if computer.get_value(parameters[0]) == 0:
        computer.counter = computer.get_value(parameters[1])
    else:
        computer.counter += len(parameters) + 1
    return StepResult.CONTINUE


JumpIfFalseOpCode = OpCode(6, 2, _jump_if_false)


def _less_than(computer: IntCodeComputer, parameters: List[Parameter]) -> StepResult:
    if computer.get_value(parameters[0]) < computer.get_value(parameters[1]):
        computer.set_value(1, parameters[2])
    else:
        computer.set_value(0, parameters[2])
    computer.counter += len(parameters) + 1
    return StepResult.CONTINUE


LessThanOpCode = OpCode(7, 3, _less_than)


def _equals(computer: IntCodeComputer, parameters: List[Parameter]) -> StepResult:
    if computer.get_value(parameters[0]) == computer.get_value(parameters[1]):
        computer.set_value(1, parameters[2])
    else:
        computer.set_value(0, parameters[2])
    computer.counter += len(parameters) + 1
    return StepResult.CONTINUE


EqualsOpCode = OpCode(8, 3, _equals)


OPCODES = [
    AddOpCode,
    MultiplyOpCode,
    HaltOpCode,
    OutputOpCode,
    InputOpCode,
    JumpIfTrueOpCode,
    JumpIfFalseOpCode,
    LessThanOpCode,
    EqualsOpCode,
]


def run(data):
    program = [int(x) for x in data.split(",")]
    computer = IntCodeComputer(program, OPCODES)
    computer.context.input.append(5)
    while not computer.run_step():
        pass
    assert len(computer.context.output) == 1
    return computer.context.output[0]

