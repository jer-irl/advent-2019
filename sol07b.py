import itertools

from sol05b import StepResult
from sol07a import IntCodeComputer, OPCODES


def calculate_output(program, setting):
    amplifiers = [IntCodeComputer(program.copy(), OPCODES) for _ in range(5)]
    for phase, amplifier in zip(setting, amplifiers):
        amplifier.context.input.append(phase)

    stage_input = [0]
    for amplifier in itertools.cycle(amplifiers):
        amplifier.context.input.extend(stage_input)
        result = amplifier.run()
        if amplifier == amplifiers[-1] and result == StepResult.HALT:
            return amplifier.context.output[-1]
        stage_input = amplifier.context.output
        amplifier.context.output = []


def run(data):
    program = [int(x) for x in data.split(",")]
    phase_settings = itertools.permutations(range(5, 10))
    return max(calculate_output(program, phase_setting) for phase_setting in phase_settings)
