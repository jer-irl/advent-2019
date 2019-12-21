"""
Dumb solution but works well enough for now.  If I feel like it, I'll change this so instead of checking every
potential password, I'll skip ahead whenever the increasing digit constraint is failed.
For 123000, skip ahead by 10 ** ((6 - 2 - 2) * 3), giving 123300, then by 10 ** ((6 - 3 - 2) * 3), giving 123330, etc.
"""


def satisfies(password):
    password_str = str(password)
    if len(password_str) != 6:
        return False

    has_pair = False
    prev_digit = int(password_str[0])
    for digit_char in password_str[1:]:
        digit = int(digit_char)
        if digit < prev_digit:
            return False
        if prev_digit == digit:
            has_pair = True

        prev_digit = digit

    if not has_pair:
        return False

    return True


def run(data):
    lowest, highest = tuple([int(x) for x in data.split("-")])
    possible = range(lowest, highest + 1)

    satisfying = 0
    for password in possible:
        if satisfies(password):
            satisfying += 1

    return satisfying
