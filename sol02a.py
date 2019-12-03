def run_prog(prog):
    for ctr in range(0, len(prog), 4):
        opcode = prog[ctr]
        if opcode == 99:
            return prog
        val1 = prog[prog[ctr + 1]]
        val2 = prog[prog[ctr + 2]]
        if opcode == 1:
            prog[prog[ctr + 3]] = val1 + val2
        elif opcode == 2:
            prog[prog[ctr + 3]] = val1 * val2
        else:
            raise RuntimeError("Bad opcode")
    raise RuntimeError("No termination")


def run(data):
    prog = [int(d) for d in data.split(",")]
    prog[1] = 12
    prog[2] = 2
    prog = run_prog(prog)
    return prog[0]
