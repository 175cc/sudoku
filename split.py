import os
import cv2


def split_image(image_path, rows, cols):
    """
    将图片分割为rows*cols块，并保存到split16文件夹中
    :param image_path: 图片路径
    :param rows: 分割行数
    :param cols: 分割列数
    :return: 分割中心点坐标列表
    """
    # 获取当前文件的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 创建输出目录的路径，指定为split16文件夹
    output_dir = os.path.join(current_dir, 'split16')
    # 如果输出目录不存在，则创建它
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 使用OpenCV读取图片
    image = cv2.imread(image_path)
    # 获取图片尺寸
    img_height, img_width, _ = image.shape

    # 计算每个分割块的尺寸
    block_width = img_width // rows
    block_height = img_height // cols

    # 分割图片并保存
    centers = []  # 创建一个列表来存储中心点坐标
    for i in range(rows):
        for j in range(cols):
            # 计算分割块的边界
            left = j * block_width
            upper = i * block_height
            right = (j + 1) * block_width
            lower = (i + 1) * block_height

            # 计算分割块的中心点坐标，起点补充(10, 215)
            center_x = left + block_width // 2 + 10
            center_y = upper + block_height // 2 + 215
            centers.append((center_x, center_y))  # 将中心点坐标添加到列表中

            # 裁剪图片
            block = image[upper:lower, left:right]

            # 构建输出文件的路径，使用split16作为子目录
            output_path = os.path.join(output_dir, f"output_{i}_{j}.png")
            # 保存图片
            cv2.imwrite(output_path, block)

    resize_split_image(rows, cols)
    return centers  # 返回中心点坐标列表


def resize_split_image(rows, cols):
    """
    不可外部调用，用于裁剪图片四周10个像素
    :param rows: 分割行数
    :param cols: 分割列数
    """
    folder_path = './split16/output_'
    img_format = '.png'
    for i in range(rows):
        for j in range(cols):
            r_ima_name = folder_path + str(i) + '_' + str(j) + img_format
            img = cv2.imread(r_ima_name)
            # print(r_ima_name)
            # 获取图像的高度和宽度
            height, width = img.shape[:2]

            # # 四周裁剪
            # 设置裁剪的宽度为10
            crop_width = 10
            # 计算裁剪后的图像的大小
            new_height = height - 2 * crop_width
            new_width = width - 2 * crop_width
            # 设置裁剪后的图像的中心位置
            center = (width / 2, height / 2)
            # 调用cv2.getRectSubPix函数，提取指定大小和中心位置的矩形区域
            cropped = cv2.getRectSubPix(img, (new_width, new_height), center)
            # 保存替换原来的图像
            cv2.imwrite(r_ima_name, cropped)

#   测试
# split_image('cropped_image.png', 4, 4)
