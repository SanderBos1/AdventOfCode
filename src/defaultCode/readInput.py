import os


def read_input(fileName: str, test: bool) -> list:
    root = os.path.dirname(os.path.abspath("src"))

    if test:
        path = os.path.join(root, "testInput", fileName)
    else:
        path = os.path.join(root, "Input", fileName)
    with open(path) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines
