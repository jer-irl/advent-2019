from sols.sol04b import satisfies


def test_satisfies():
    assert satisfies(112233)
    assert not satisfies(123444)
    assert satisfies(111122)
