from src.opdrachten_2024 import part_4a, part_4b


def test_opdracht_4a():
    result = 18
    assert part_4a(True) == result


def test_opdracht_4a_real():
    result = 2401
    assert part_4a() == result


def test_opdracht_4b():
    result = 9
    assert part_4b(True) == result


def test_opdracht_4b_real():
    result = 1822
    assert part_4b() == result
