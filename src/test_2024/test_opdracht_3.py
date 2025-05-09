from src.opdrachten_2024 import part_3a, part_3b


def test_opdracht_3a():
    result = 161
    assert part_3a(True) == result


def test_opdracht_3a_real():
    result = 173517243
    assert part_3a() == result


def test_opdracht_3b():
    result = 48
    assert part_3b(True) == result


def test_opdracht_3b_real():
    result = 100450138
    assert part_3b() == result
