from . import IntCodeComputer, OPCODES


def run_prog(prog):
    computer = IntCodeComputer(prog, OPCODES)
    while not computer.run_step():
        pass
    return list(computer.state[x] for x in sorted(computer.state.keys()))


def run(data):
    prog = [int(d) for d in data.split(",")]
    prog[1] = 12
    prog[2] = 2
    prog = run_prog(prog)
    return prog[0]
