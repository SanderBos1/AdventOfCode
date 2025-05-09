from src.defaultCode import read_input


def common_4(test):
    lines = read_input("2024/opdracht4.txt", test)
    matrix = [list(row) for row in lines]
    return matrix


def part_4a(test=False):
    total = 0
    matrix = common_4(test)
    rows, cols = len(matrix), len(matrix[0])
    targets = {"XMAS", "SAMX"}

    directions = [
        (0, 1),   # Horizontal (→)
        (1, 0),   # Vertical (↓)
        (1, 1),   # Diagonal ↘
        (-1, 1)   # Diagonal ↗
    ]
    
    for i in range(rows):
        for j in range(cols):
            for di, dj in directions:
                word = []
                for k in range(4):
                    ni, nj = i + di * k, j + dj * k
                    if 0 <= ni < rows and 0 <= nj < cols:
                        word.append(matrix[ni][nj])
                    else:
                        break
                if "".join(word) in targets:
                    total += 1
    return total


def part_4b(test=False):
    total = 0
    matrix = common_4(test)
    rows, cols = len(matrix), len(matrix[0])
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if matrix[i][j] == "A":
                diagonals = [
                    (matrix[i-1][j-1], matrix[i+1][j+1]),
                    (matrix[i-1][j+1], matrix[i+1][j-1])
                ]
                if all(set(pair) == {"M", "S"} for pair in diagonals):
                    total += 1
    return total
