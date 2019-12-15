from sol01a import fuel_for_mass


def test_fuel_for_mass():
    assert fuel_for_mass(12) == 2
    assert fuel_for_mass(14) == 2
    assert fuel_for_mass(1969) == 654
    assert fuel_for_mass(100756) == 33583
