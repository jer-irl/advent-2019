from collections import defaultdict
import math

from sols.sol10a import gcd, get_asteroids, visible_asteroids


def get_vaporizations(asteroids, station):
    slope_buckets = defaultdict(list)
    for asteroid in asteroids:
        drow, dcol = asteroid[0] - station[0], asteroid[1] - station[1]
        if drow == 0 and dcol == 0:
            divisor = 1
        else:
            divisor = abs(gcd(drow, dcol))
        slope_buckets[(drow / divisor, dcol / divisor)].append(asteroid)

    for bucket in slope_buckets.values():
        bucket.sort(key=lambda a: abs(gcd(a[0], a[1])))

    angle_buckets = dict()
    for key, val in slope_buckets.items():
        angle_buckets[math.atan2(key[1], key[0])] = val

    items = list(angle_buckets.items())
    items.sort(key=lambda item: item[0])
    sorted_buckets = [item[1] for item in items]

    vaporized = []
    while any(len(bucket) > 0 for bucket in sorted_buckets):
        for bucket in sorted_buckets:
            if len(bucket) == 0:
                continue
            vaporized.append(bucket.pop(0))

    return vaporized


def run(data):
    asteroids = get_asteroids(data)
    station = max(asteroids, key=lambda a: visible_asteroids(a, asteroids))
    vaporizations = get_vaporizations(asteroids, station)
