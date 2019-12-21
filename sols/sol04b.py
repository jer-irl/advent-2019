from sols.sol04a import satisfies as satisfies_a


def satisfies(password):
    if not satisfies_a(password):
        return False

    run_char = None
    run_count = 0
    for c in str(password):
        if c != run_char:
            if run_count == 2:
                return True
            run_char = c
            run_count = 1
        else:
            run_count += 1
    return run_count == 2


def run(data):
    lowest, highest = tuple([int(x) for x in data.split("-")])
    return len([x for x in range(lowest, highest + 1) if satisfies(x)])
