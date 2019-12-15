from dataclasses import dataclass
import enum
from typing import Dict, Callable, List


class ParameterMode(enum.IntEnum):
    POSITION = 0
    IMMEDIATE = 1


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
        self.state = state
        self.counter = 0
        self.opcodes: Dict[int, OpCode] = dict((opcode.code, opcode) for opcode in opcodes)
        self.context = ComputerContext()

    def run_step(self) -> StepResult:
        """Returns True if should terminate"""
        op = self.state[self.counter]
        opcode = self.opcodes[int(str(op)[-2:])]
        parameter_modes = [ParameterMode(int(c)) for c in str(op).zfill(opcode.num_parameters + 2)[:-2]]
        assert len(parameter_modes) == opcode.num_parameters
        pairs = zip(reversed(parameter_modes), self.state[self.counter + 1:self.counter + 1 + opcode.num_parameters])
        parameters = [Parameter(mode, value) for (mode, value) in pairs]
        return opcode.run(self, parameters)

    def get_value(self, parameter: Parameter) -> int:
        if parameter.mode == ParameterMode.POSITION:
            return self.state[parameter.value]
        elif parameter.mode == ParameterMode.IMMEDIATE:
            return parameter.value
        else:
            raise NotImplementedError()

    def set_value(self, value: int, parameter: Parameter):
        if parameter.mode == ParameterMode.POSITION:
            self.state[parameter.value] = value
        elif parameter.mode == ParameterMode.IMMEDIATE:
            raise RuntimeError()
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


def run_prog(prog):
    computer = IntCodeComputer(prog, [AddOpCode, MultiplyOpCode, HaltOpCode])
    while not computer.run_step():
        pass
    return computer.state


def run(data):
    prog = [int(d) for d in data.split(",")]
    prog[1] = 12
    prog[2] = 2
    prog = run_prog(prog)
    return prog[0]
