import subprocess
import cv2
import split
from shudu import sudoku_square_grid_confirm


# 使用match和case关键字实现switch，case分支
def sudoku_square_grid(no):
    match no:
        case 4:
            split_number = 4
            rows_r, cols_c = 4, 4
        case 6:
            split_number = 6
            rows_r, cols_c = 6, 6
        case 9:
            split_number = 9
            rows_r, cols_c = 9, 9
        case _:
            print("请确认数独x宫格模式： 4,6,9")
            return None  # 如果输入不合法，返回None
            # 使用元组返回三个值
    return split_number, rows_r, cols_c


def get_convert_cut_screenshot():
    """
    从手机adb截图，裁剪二值化
    """
    # 定义截图的文件名和存放路径
    screenshot_name = "screenshot.png"
    screenshot_path = "F:\\Study_Zone\\shudu\\"  # 替换为你的指定目录
    # 构建ADB截图命令
    adb_command = f"adb shell screencap -p /sdcard/{screenshot_name}"
    # 执行截图命令
    subprocess.run(adb_command, shell=True)
    # 将截图从设备传输到电脑
    adb_pull_command = f"adb pull /sdcard/{screenshot_name} {screenshot_path}"
    subprocess.run(adb_pull_command, shell=True)

    # 读取图像
    img2 = cv2.imread(screenshot_path + screenshot_name)  # 替换为你的图像路径
    # 灰度化后二值化
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    _, binary_gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 定义ROI，格式为[y:y+h, x:x+w]
    # x和y是ROI左上角的坐标，w和h是ROI的宽度和高度
    x, y, w, h = 54, 220, 972, 972  # 根据需要替换这些值
    # 从原始图像中裁剪出ROI区域
    new_x, new_y = x, y
    new_w, new_h = w, h
    # 裁剪图像
    crop_img = binary_gray[new_y:new_y + new_h, new_x:new_x + new_w]
    # 保存裁剪后的图像
    cv2.imwrite('wait_split.png', crop_img)  # 替换为你的保存路径


def coordinate_matrix():
    """
    获取坐标矩阵
    分割图片，获取中心坐标
    :return: 分割图中心坐标矩阵   二维列表
    """
    # 参数传递; 宫格确认
    _, rows_r, cols_c = sudoku_square_grid(sudoku_square_grid_confirm)
    # 调用函数，传入图片路径和分割行列数
    centers = split.split_image('wait_split.png', rows_r, cols_c)

    # 将centers列表转换为  r x c 的二维数组
    centers_2d = [centers[i:i + rows_r] for i in range(0, len(centers), cols_c)]
    # 打印二维数组以验证
    print('坐标矩阵：')
    for row in centers_2d:
        print(row)
    return centers_2d
