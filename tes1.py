import cv2

# 读取图片
img = cv2.imread("5.png")

# 转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Crop the top half of the image
height, width = binary.shape
binary = binary[0:height // 2, 0:width]

# 找到所有的轮廓
_, contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 筛选出滑块和目标区域的轮廓
# 这里假设滑块和目标区域的轮廓是面积最大的两个轮廓
contours.sort(key=cv2.contourArea, reverse=True)
slider_contour = contours[0]
target_contour = contours[1]

# 绘制轮廓
dst = cv2.drawContours(img, [slider_contour, target_contour], -1, (0, 0, 255), 3)

# 显示结果
cv2.imshow("dst", dst)
cv2.waitKey(0)
