import subprocess
from PIL import Image
import pytesseract
import cv2


# 定义截图和裁剪的函数
def screennext_and_crop(screennext_path, crop_area):
    # 构建ADB截图命令
    adb_command = f"adb shell screencap -p /sdcard/screennext.png"
    # 执行截图命令
    subprocess.run(adb_command, shell=True)
    # 将截图从设备传输到电脑
    adb_pull_command = f"adb pull /sdcard/screennext.png {screennext_path}"
    subprocess.run(adb_pull_command, shell=True)
    # 使用OpenCV读取图像
    img = cv2.imread(screennext_path + 'screennext.png')
    # 裁剪图片
    x, y, w, h = crop_area  # 解包裁剪区域
    x, y, w, h = 180, 890, 240, 80
    cropped_image_next = img[y:y + h, x:x + w]
    # 保存裁剪后的图片
    # cv2.imshow("naem", cropped_image_next)
    # cv2.waitKey(0)

    cv2.imwrite(screennext_path + 'cropped_screennext.png', cropped_image_next)
    return screennext_path + 'cropped_screennext.png'


# 定义OCR识别的函数
def ocr_recognition(cropped_image_next_path):
    # 设置Tesseract路径
    pytesseract.pytesseract.tesseract_cmd = r'D:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    # 打开裁剪后的图片
    img = Image.open(cropped_image_next_path)
    # OCR识别
    text = pytesseract.image_to_string(img, lang='chi_sim')  # 假设文字是简体中文
    return text


# 定义点击操作的函数
def tap_screen(x, y):
    # 使用ADB命令模拟点击操作
    adb_tap_command = f"adb shell input tap {x} {y}"
    subprocess.run(adb_tap_command, shell=True)


# 主函数
def main():
    # 指定截图存放路径和裁剪区域
    screennext_path = "F:\\Study_Zone\\shudu\\"  # 替换为你的指定目录
    crop_area = (180, 890, 240, 80)  # 替换为你的裁剪区域
    # 截图并裁剪
    cropped_image_next_path = screennext_and_crop(screennext_path, crop_area)
    # OCR识别
    text = ocr_recognition(cropped_image_next_path)
    print(text)
    # 如果识别到了“下一关”字样，进行点击操作
    if "下一关" in text:
        # 替换为“下一关”字样在屏幕上的坐标
        x = 0
        y = 0
        print('OK')
        # tap_screen(x, y)


if __name__ == '__main__':
    main()
