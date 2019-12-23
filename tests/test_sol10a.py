from sols.sol10a import get_asteroids, max_visible, visible_asteroids


board1 = \
"""......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""


board2 = \
"""#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###."""


board3 = \
""".#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""


board4 = \
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


board5 = \
""".#..#
.....
#####
....#
...##"""


def test_max_visible():
    assert max_visible(get_asteroids(board1)) == 33
    assert max_visible(get_asteroids(board2)) == 35
    assert max_visible(get_asteroids(board3)) == 41
    assert max_visible(get_asteroids(board4)) == 210
    assert max_visible(get_asteroids(board5)) == 8
