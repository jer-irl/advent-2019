from collections import defaultdict
from dataclasses import dataclass
import enum
from typing import Dict, Callable, List


class ParameterMode(enum.IntEnum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class StepResult(enum.IntEnum):
    CONTINUE = 0
    HALT = 1
    INPUT = 2


@dataclass
class Parameter:
    mode: ParameterMode
    value: int


class ComputerContext:
    def __init__(self):
        self.input = list()
        self.output = list()


@dataclass
class OpCode:
    code: int
    num_parameters: int
    run: Callable[["IntCodeComputer", List[Parameter], ComputerContext], StepResult]


class IntCodeComputer:
    def __init__(self, state: List[int], opcodes: List[OpCode]):
        self.state = defaultdict(int)
        for i, x in enumerate(state):
            self.state[i] = x
        self.counter = 0
        self.opcodes: Dict[int, OpCode] = dict((opcode.code, opcode) for opcode in opcodes)
        self.context = ComputerContext()
        self.relative_base = 0

    def run_step(self) -> StepResult:
        """Returns True if should terminate"""
        op = self.state[self.counter]
        opcode = self.opcodes[int(str(op)[-2:])]
        parameter_modes = [ParameterMode(int(c)) for c in str(op).zfill(opcode.num_parameters + 2)[:-2]]
        assert len(parameter_modes) == opcode.num_parameters
        pairs = zip(
            reversed(parameter_modes),
            [self.state[x] for x in range(self.counter + 1, self.counter + 1 + opcode.num_parameters)]
        )
        parameters = [Parameter(mode, value) for (mode, value) in pairs]
        return opcode.run(self, parameters)

    def get_value(self, parameter: Parameter) -> int:
        if parameter.mode == ParameterMode.POSITION:
            return self.state[parameter.value]
        elif parameter.mode == ParameterMode.IMMEDIATE:
            return parameter.value
        elif parameter.mode == ParameterMode.RELATIVE:
            return self.state[self.relative_base + parameter.value]
        else:
            raise NotImplementedError()

    def set_value(self, value: int, parameter: Parameter):
        if parameter.mode == ParameterMode.POSITION:
            self.state[parameter.value] = value
        elif parameter.mode == ParameterMode.IMMEDIATE:
            raise RuntimeError()
        elif parameter.mode == ParameterMode.RELATIVE:
            self.state[self.relative_base + parameter.value] = value
        else:
            raise NotImplementedError()

    def run(self) -> StepResult:
        while (result := self.run_step()) == StepResult.CONTINUE:
            pass
        return result


def _add(computer: IntCodeComputer, parameters: List[Parameter]) -> StepResult:
    input1 = computer.get_value(parameters[0])
    input2 = computer.get_value(parameters[1])
    computer.set_value(input1 + input2, parameters[2])
    computer.counter += 4
    return StepResult.CONTINUE


AddOpCode = OpCode(1, 3, _add)


def _multiply(computer: IntCodeComputer, parameters: List[Parameter]) -> StepResult:
    input1 = computer.get_value(parameters[0])
    input2 = computer.get_value(parameters[1])
    computer.set_value(input1 * input2, parameters[2])
    computer.counter += 4
    return StepResult.CONTINUE


MultiplyOpCode = OpCode(2, 3, _multiply)


def _halt(computer: IntCodeComputer, parameters: List[Parameter]) -> StepResult:
    return StepResult.HALT


HaltOpCode = OpCode(99, 0, _halt)


def _input(computer: IntCodeComputer, parameters: List[Parameter]) -> StepResult:
    if len(computer.context.input) == 0:
        return StepResult.INPUT
    input_value = computer.context.input.pop(0)
    computer.set_value(input_value, parameters[0])
    computer.counter += 2
    return StepResult.CONTINUE


InputOpCode = OpCode(3, 1, _input)


def _output(computer: IntCodeComputer, parameters: List[Parameter]) -> StepResult:
    output_value = computer.get_value(parameters[0])
    computer.context.output.append(output_value)
    computer.counter += 2
    return StepResult.CONTINUE


OutputOpCode = OpCode(4, 1, _output)


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


def _adjust_relative_base(computer: IntCodeComputer, parameters: List[Parameter]) -> StepResult:
    computer.relative_base += computer.get_value(parameters[0])
    computer.counter += len(parameters) + 1
    return StepResult.CONTINUE


AdjustRelativeBaseOpCode = OpCode(9, 1, _adjust_relative_base)


OPCODES = [
    AddOpCode,
    MultiplyOpCode,
    HaltOpCode,
    InputOpCode,
    OutputOpCode,
    JumpIfTrueOpCode,
    JumpIfFalseOpCode,
    EqualsOpCode,
    LessThanOpCode,
    AdjustRelativeBaseOpCode
]
