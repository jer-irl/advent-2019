from . import IntCodeComputer, OPCODES


def run_prog(program):
    computer = IntCodeComputer(program, OPCODES)
    computer.context.input.append(1)
    while not computer.run_step():
        pass
    output = computer.context.output
    assert all(x == 0 for x in output[:-1])
    return output[-1]


def run(data):
    program = [int(x) for x in data.split(",")]
    return run_prog(program)
