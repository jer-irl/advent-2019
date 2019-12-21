from . import IntCodeComputer, OPCODES


def run_program(program, input):
    computer = IntCodeComputer(program, OPCODES)
    computer.context.input = input
    computer.run()
    return computer.context.output


def run(data):
    program = [int(x) for x in data.split(",")]
    output = run_program(program, [1])
    assert len(output) == 1
    return output[0]
