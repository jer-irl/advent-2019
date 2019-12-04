from sol03a import (
    construct_steps,
    construct_locations,
    get_segments,
    get_intersections,
)


def steps_to_point(point, segments):
    distance = 0
    for start, end in segments:
        if start[0] == end[0]:
            if start[0] == point[0]:
                if start[1] < end[1] and start[1] < point[1] <= end[1]:
                    return distance + point[1] - start[1]
                elif end[1] < start[1] and end[1] <= point[1] < start[1]:
                    return distance + start[1] - point[1]
            distance += abs(start[1] - end[1])
        elif start[1] == end[1]:
            if start[1] == point[1]:
                if start[0] < end[0] and start[0] < point[0] <= end[0]:
                    return distance + point[0] - start[0]
                elif end[0] < start[0] and end[0] <= point[0] < start[0]:
                    return distance + start[0] - point[0]
            distance += abs(start[0] - end[0])
        else:
            raise RuntimeError()
    raise RuntimeError()


def run(data):
    wires = data.split()
    steps = [construct_steps(wire) for wire in wires]
    locations = [construct_locations(step_list) for step_list in steps]
    segments = [get_segments(segment_list) for segment_list in locations]
    intersections = [s for s in get_intersections(*segments) if s != (0, 0)]

    return min(steps_to_point(i, segments[0]) + steps_to_point(i, segments[1]) for i in intersections)
