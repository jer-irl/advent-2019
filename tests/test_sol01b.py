from sols.sol01b import total_fuel_for_mass


def test_total_fuel_for_mass():
    assert total_fuel_for_mass(14) == 2
    assert total_fuel_for_mass(1969) == 966
    assert total_fuel_for_mass(100756) == 50346
