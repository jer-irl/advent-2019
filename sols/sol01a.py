import math


def fuel_for_mass(mass):
    return math.floor(mass / 3) - 2


def run(data):
    return sum(fuel_for_mass(int(mass)) for mass in data.split())
