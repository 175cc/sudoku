# 定义一个9x9的数独矩阵，0表示空格
sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# 定义一个函数，检查给定的数字是否在给定的行中
def check_row(row, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return False
    return True


# 定义一个函数，检查给定的数字是否在给定的列中
def check_col(col, num):
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    return True


# 定义一个函数，检查给定的数字是否在给定的3x3的小方格中
def check_box(row, col, num):
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if sudoku[i][j] == num:
                return False
    return True


# 定义一个函数，检查给定的数字是否可以放在给定的位置
def check_place(row, col, num):
    return check_row(row, num) and check_col(col, num) and check_box(row, col, num)


# 定义一个函数，找到一个空格的位置，如果没有空格，返回(-1, -1)
def find_empty():
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return -1, -1


# 定义一个函数，用回溯法解决数独
def solve():
    row, col = find_empty()
    if row == -1 and col == -1:
        return True, sudoku  # 如果没有空格，返回True和数独矩阵
    for num in range(1, 10):
        if check_place(row, col, num):
            sudoku[row][col] = num
            solved, solution = solve()
            if solved:
                return True, solution
            sudoku[row][col] = 0
    return False, None


# 定义一个函数，打印数独矩阵
def print_sudoku():
    print("解决方案：")
    for row in sudoku:
        print(row)
