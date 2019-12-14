"""
Memoize results in a cache.
"""


def orbits_per_node(cache, parents, node):
    if node == "COM":
        return 0
    if node in cache:
        return cache[node]
    parent = parents[node]
    result = orbits_per_node(cache, parents, parent) + 1
    cache[node] = result
    return result


def run(data):
    orbits = [tuple(x.split(")")) for x in data.split()]
    parents = {x[1]: x[0] for x in orbits}
    cache = {}
    return sum(orbits_per_node(cache, parents, node) for node in parents.keys())
