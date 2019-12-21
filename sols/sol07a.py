import itertools

from sols.sol05b import IntCodeComputer, OPCODES


def calculate_output(program, setting):
    stage_input = 0
    for i in range(5):
        computer = IntCodeComputer(program, OPCODES)
        computer.context.input.append(setting[i])
        computer.context.input.append(stage_input)
        computer.run()
        assert len(computer.context.output) == 1
        stage_output = computer.context.output[0]
        stage_input = stage_output
    return stage_input


def run(data):
    program = [int(x) for x in data.split(",")]
    settings = itertools.permutations(range(5))

    return max(calculate_output(program, setting) for setting in settings)
