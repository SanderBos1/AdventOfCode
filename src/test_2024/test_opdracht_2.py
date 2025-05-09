from src.opdrachten_2024 import part_2a, part_2b


def test_opdracht_2a():
    result = 2
    assert part_2a(True) == result


def test_opdracht_2a_real():
    result = 269
    assert part_2a() == result


def test_opdracht_2b():
    result = 4
    assert part_2b(True) == result


def test_opdracht_2b_real():
    result = 337
    assert part_2b() == result
