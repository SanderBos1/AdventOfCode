from src.opdrachten_2024 import part_1a, part_1b


def test_opdracht_1a():
    result = 11
    assert part_1a(True) == result


def test_opdracht_1a_real():
    result = 1388114
    assert part_1a() == result


def test_opdracht_1b():
    result = 31
    assert part_1b(True) == result


def test_opdracht_1b_real():
    result = 23529853
    assert part_1b() == result
