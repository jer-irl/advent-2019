def get_asteroids(data):
    asteroids = []
    for row_idx, row in enumerate(data.split("\n")):
        for col_idx, c in enumerate(row):
            if c == "#":
                asteroids.append((row_idx, col_idx))
    return asteroids


def gcd(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    return gcd(y, x % y)


def visible_asteroids(asteroid, asteroids):
    visible_angles = set()
    for candidate in asteroids:
        drow, dcol = asteroid[0] - candidate[0], asteroid[1] - candidate[1]
        if drow == 0 and dcol == 0:
            continue
        divisor = abs(gcd(drow, dcol))
        visible_angles.add((drow / divisor, dcol / divisor))

    return len(visible_angles)


def max_visible(asteroids):
    return max(visible_asteroids(asteroid, asteroids) for asteroid in asteroids)


def run(data):
    asteroids = get_asteroids(data)
    return max_visible(asteroids)
