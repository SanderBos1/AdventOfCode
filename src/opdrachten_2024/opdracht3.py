from src.defaultCode import read_input
import re


def common_3(test):
    lines = read_input("2024/opdracht3.txt", test)
    return ''.join(line.strip() for line in lines)


def sum_commmands(line):
    total = 0
    commands = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
    for a, b in commands:
        total += int(a) * int(b)
    return total


def part_3a(test=False):
    line = common_3(test)
    return sum_commmands(line)


def part_3b(test=False):
    line = common_3(test)
    total = 0
    splitcheck = line.split("don\'t()")
    for i in range(len(splitcheck)):
        if i == 0:
            total = total + sum_commmands(splitcheck[i])
        else:
            match = re.search(r"do()", splitcheck[i])
            if match:
                total = total + sum_commmands(splitcheck[i][match.start():])
    return total
