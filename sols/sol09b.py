from sols.sol09a import run_program


def run(data):
    program = [int(x) for x in data.split(",")]
    result = run_program(program, [2])
    assert len(result) == 1
    return result[0]
