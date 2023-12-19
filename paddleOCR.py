from paddleocr import PaddleOCR, draw_ocr
import time

current_time = time.time()
local_time = time.localtime(current_time)
minute = local_time.tm_min
second = local_time.tm_sec
# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`

img_path = r'F:\Study_Zone\shudu\cropped_image.png'
ocr = PaddleOCR(use_gpu=False, use_angle_cls=False,
                lang="ch", rec_model_dir="./model/ch_PP-OCRv3_rec/")
result = ocr.ocr('cropped_image.png', det=False)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# 显示结果
from PIL import Image

result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path=r'F:\Study_Zone\PaddleOCR-2.7.0\fonts\Microsoft_Yahei.ttf')
im_show = Image.fromarray(im_show)
im_show.save('re11.jpg')

current_time = time.time()
local_time = time.localtime(current_time)
minute = local_time.tm_min
second = local_time.tm_sec
