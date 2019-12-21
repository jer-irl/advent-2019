"""
Acyclic which makes this easier
"""

from collections import defaultdict


def distance(adjacencies, start, target, prev, depth):
    depth = depth + 1
    if start == target:
        return depth
    if len(adjacencies[start]) == 1 and adjacencies[start][0] == prev:
        return None
    for next_node in adjacencies[start]:
        if next_node == prev:
            continue
        if (result := distance(adjacencies, next_node, target, start, depth)) is not None:
            return result
    return None


def run(data):
    adjacencies = [tuple(x.split(")")) for x in data.split()]
    accessible_nodes = defaultdict(list)
    for x, y in adjacencies:
        accessible_nodes[x].append(y)
        accessible_nodes[y].append(x)

    target = "SAN"
    start = "YOU"

    return distance(accessible_nodes, start, target, None, 0) - 3
