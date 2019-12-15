from typing import List

from sol02a import IntCodeComputer, OpCode, AddOpCode, MultiplyOpCode, HaltOpCode, Parameter, StepResult


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


def run_prog(program):
    computer = IntCodeComputer(program, [AddOpCode, MultiplyOpCode, HaltOpCode, InputOpCode, OutputOpCode])
    computer.context.input.append(1)
    while not computer.run_step():
        pass
    output = computer.context.output
    assert all(x == 0 for x in output[:-1])
    return output[-1]


def run(data):
    program = [int(x) for x in data.split(",")]
    return run_prog(program)
