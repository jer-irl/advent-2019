from sols.sol09a import run_program


def test_run_program_9a():
    assert (run_program([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99], [])
            == [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99])
    output1 = run_program([1102, 34915192, 34915192, 7, 4, 7, 99, 0], [])
    assert len(output1) == 1
    assert len(str(output1[0])) == 16
    output2 = run_program([104, 1125899906842624, 99], [])
    assert len(output2) == 1
    assert output2[0] == 1125899906842624
