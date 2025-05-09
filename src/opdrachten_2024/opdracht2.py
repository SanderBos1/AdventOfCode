from src.defaultCode import read_input


def common_2(test):
    lines = read_input("2024/opdracht2.txt", test)
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split(" ")
        lines[i] = [int(x) for x in lines[i]]
    return lines


def safe_rule(arr):
    ascending = True
    descending = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            ascending = False
        if arr[i] < arr[i+1]:
            descending = False
        if abs(arr[i] - arr[i+1]) > 3 or abs(arr[i] - arr[i+1]) < 1:
            return False
    return ascending or descending


def part_2a(test=False):
    sum = 0
    lines = common_2(test)
    for report in lines:
        if safe_rule(report):
            sum += 1
    return sum


def part_2b(test=False):
    sum = 0
    lines = common_2(test)
    for report in lines:
        for i in range(len(report)):
            if safe_rule(report[:i] + report[i+1:]):
                sum += 1
                break
    return sum