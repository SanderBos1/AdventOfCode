from src.defaultCode import read_input


def common_a(test):
    lines = read_input("2024/opdracht1.txt", test)
    leftList = []
    rightList = []
    for line in lines:
        left, right = map(int, line.split())
        leftList.append(int(left))
        rightList.append(int(right))
    return leftList, rightList


def part_1a(test=False):
    result = 0
    leftList, rightList = common_a(test)
    for x, y in zip(sorted(leftList), sorted(rightList)):
        result = result + abs(x - y)
    return result


def part_1b(test=False):
    result = 0
    leftList, rightList = common_a(test)
    for i in range(len(leftList)):
        appearance = rightList.count(leftList[i])
        result = result + leftList[i] * appearance
    return result