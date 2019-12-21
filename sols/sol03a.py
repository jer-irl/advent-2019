import itertools


def movement_from_step(step):
    directions = {
        "L": (-1, 0),
        "R": (1, 0),
        "U": (0, 1),
        "D": (0, -1)
    }
    dx, dy = directions[step[0]]
    length = int(step[1:])
    return dx * length, dy * length


def construct_steps(wire):
    return [movement_from_step(step) for step in wire.split(",")]


def construct_locations(steps):
    wire_locations = [(0, 0)]
    for dx, dy in steps:
        prev_x, prev_y = wire_locations[-1]
        wire_locations.append((prev_x + dx, prev_y + dy))
    return wire_locations


def get_segments(locations):
    return [(locations[i], locations[i + 1]) for i in range(len(locations) - 1)]


def get_vertical_horizontal(segments):
    vertical = []
    horizontal = []
    for start, end in segments:
        if start[0] == end[0]:
            vertical.append((start, end) if start[1] < end[1] else (end, start))
        else:
            horizontal.append((start, end) if start[0] < end[0] else (end, start))
    return vertical, horizontal


def do_intersect(vertical, horizontal):
    return (vertical[0][1] <= horizontal[0][1] <= vertical[1][1]
            and horizontal[0][0] <= vertical[0][0] <= horizontal[1][0])


def intersection(v, h):
    return v[0][0], h[0][1]


def get_intersections(segments1, segments2):
    vertical1, horizontal1 = get_vertical_horizontal(segments1)
    vertical2, horizontal2 = get_vertical_horizontal(segments2)
    combinations = itertools.chain(itertools.product(vertical1, horizontal2), itertools.product(vertical2, horizontal1))
    return set(intersection(v, h) for v, h in combinations if do_intersect(v, h))


def run(data):
    wires = data.split()
    steps = [construct_steps(wire) for wire in wires]
    locations = [construct_locations(step_list) for step_list in steps]
    segments = [get_segments(segment_list) for segment_list in locations]
    intersections = [s for s in get_intersections(*segments) if s != (0, 0)]
    return min(*[s for i in intersections if (s := abs(i[0]) + abs(i[1])) > 0])
