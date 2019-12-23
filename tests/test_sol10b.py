from sols.sol10b import get_asteroids, get_vaporizations, visible_asteroids


board =\
""".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""


def test_get_vaporizations():
    asteroids = get_asteroids(board)
    station = max(asteroids, key=lambda a: visible_asteroids(a, asteroids))
    print(station)
    vaporizations = get_vaporizations(asteroids, station)

    assert vaporizations[0] == (11, 12)
    assert vaporizations[1] == (12, 1)
    assert vaporizations[2] == (12, 2)
    assert vaporizations[9] == (12, 8)
    assert vaporizations[19] == (16, 0)
    assert vaporizations[49] == (16, 9)
    assert vaporizations[99] == (10, 16)
    assert vaporizations[198] == (9, 6)
    assert vaporizations[199] == (8, 2)
    assert vaporizations[200] == (10, 9)
    assert vaporizations[298] == (11, 1)
