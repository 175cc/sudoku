# 定义一个6x6的数独矩阵，0表示空格
sudoku = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]


# 定义一个函数，检查给定的数字是否在给定的行中
def check_row(row, num):
    # 遍历行中的每个元素
    for i in range(6):
        # 如果元素等于数字，返回False
        if sudoku[row][i] == num:
            return False
    # 否则返回True
    return True


# 定义一个函数，检查给定的数字是否在给定的列中
def check_col(col, num):
    # 遍历列中的每个元素
    for i in range(6):
        # 如果元素等于数字，返回False
        if sudoku[i][col] == num:
            return False
    # 否则返回True
    return True


# 定义一个函数，检查给定的数字是否在给定的3x2的小方格中
def check_box(row, col, num):
    # 计算小方格的起始行和列
    row_start = (row // 2) * 2
    col_start = (col // 3) * 3
    # 遍历小方格中的每个元素
    for i in range(row_start, row_start + 2):
        for j in range(col_start, col_start + 3):
            # 如果元素等于数字，返回False
            if sudoku[i][j] == num:
                return False
    # 否则返回True
    return True


# 定义一个函数，检查给定的数字是否可以放在给定的位置
def check_place(row, col, num):
    # 检查行，列和小方格，如果都为True，返回True，否则返回False
    return check_row(row, num) and check_col(col, num) and check_box(row, col, num)


# 定义一个函数，找到一个空格的位置，如果没有空格，返回(-1, -1)
def find_empty():
    # 遍历数独矩阵中的每个元素
    for i in range(6):
        for j in range(6):
            # 如果元素为0，返回其位置
            if sudoku[i][j] == 0:
                return i, j
    # 如果没有空格，返回(-1, -1)
    return -1, -1


# 定义一个函数，用回溯法解决数独
def solve():
    # 找到一个空格的位置
    row, col = find_empty()
    # 如果没有空格，说明数独已经解决，返回True和数独矩阵
    if row == -1 and col == -1:
        return True, sudoku  # 递归的出口
    # 否则，尝试1到6中的每个数字
    for num in range(1, 7):
        # 检查数字是否可以放在空格处
        if check_place(row, col, num):
            # 如果可以，将数字放入空格
            sudoku[row][col] = num
            # 递归地尝试解决剩余的数独
            solved, solution = solve()
            if solved:
                # 如果成功，返回True和数独矩阵
                return True, solution
            # 如果失败，将空格还原为0，回溯
            sudoku[row][col] = 0
    # 如果所有数字都不能放在空格处，返回False和None
    return False, None


# 定义一个函数，打印数独矩阵
def print_sudoku():
    print("解决方案：")
    for row in sudoku:
        print(row)
