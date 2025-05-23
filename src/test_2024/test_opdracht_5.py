from src.opdrachten_2024 import part_5a, part_5b


def test_opdracht_5a():
    result = 143
    assert part_5a(True) == result


def test_opdracht_5a_real():
    result = 6949
    assert part_5a() == result


def test_opdracht_5b():
    result = 123
    assert part_5b(True) == result


def test_opdracht_5b_real():
    result = 4145
    assert part_5b() == result
