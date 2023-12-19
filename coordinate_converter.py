# coordinate_converter.py

def convert_coordinates(x, y, original_resolution, target_resolution):
    """
    转换坐标从原始分辨率到目标分辨率。

    :param x: 原始x坐标
    :param y: 原始y坐标
    :param original_resolution: (width, height)原始分辨率
    :param target_resolution: (width, height)目标分辨率
    :return: (x, y)转换后的坐标
    """
    original_width, original_height = original_resolution
    target_width, target_height = target_resolution

    # 计算宽度和高度的缩放比例
    scale_width = target_width / original_width
    scale_height = target_height / original_height

    # 应用缩放比例
    new_x = int(x * scale_width)
    new_y = int(y * scale_height)

    return new_x, new_y
