import itertools
from sols.sol02a import run_prog


def run(data):
    target = 19690720
    prog = [int(d) for d in data.split(",")]
    for cnt in itertools.count(0, 1):
        for i in range(cnt + 1):
            noun = cnt - i
            verb = i
            test_prog = prog.copy()
            test_prog[1] = noun
            test_prog[2] = verb
            result = run_prog(test_prog)[0]
            if result == target:
                return 100 * noun + verb
