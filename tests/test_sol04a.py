from sol04a import satisfies


def test_satisfies():
    assert satisfies(111111)
    assert not satisfies(223450)
    assert not satisfies(123789)
    assert not satisfies(123)
