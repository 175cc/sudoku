import numpy as np
from paddleocr import PaddleOCR


def padddleocr_result():
    """
    识别结果
    :return: OCR识别结果矩阵·
    """
    # 创建一个9x9的二维数组
    result = np.zeros((9, 9), dtype=int)
    # 创建一个OCR对象
    ocr = PaddleOCR(use_gpu=False, use_angle_cls=False, lang="ch")
    # 遍历所有的图片
    for i in range(9):
        for j in range(9):
            # 构造图片的文件名
            img_path = f"split16/output_{i}_{j}.png"

            # 使用OCR识别图片中的数字
            content = ocr.ocr(img_path, det=False)

            # 如果识别结果为空，我们将其视为0
            if not content or not content[0][0][0]:
                result[i][j] = 0
            else:
                # 否则我们将识别的数字存入二维数组的对应位置
                # 在这里添加一个过滤步骤，只保留数字
                if content[0][0][0].isdigit():
                    result[i][j] = int(content[0][0][0])
                else:
                    result[i][j] = 0

    # 打印二维数组
    print(result)
    return result
