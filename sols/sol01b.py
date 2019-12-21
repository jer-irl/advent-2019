from sols.sol01a import fuel_for_mass


def total_fuel_for_mass(mass):
    result = 0
    m = mass
    # My first time using the Python 3.8 walrus operator!
    while (fuel := fuel_for_mass(m)) > 0:
        result += fuel
        m = fuel
    return result


def run(data):
    return sum(total_fuel_for_mass(int(m)) for m in data.split())
