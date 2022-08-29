import cv2
from cv2 import cv2

# 读取图片
image=cv2.imread(r'./images/7921.png')#图片路径不能为中文
# 显示图片
cv2.imshow('input image',image)
# 等待键盘输入，单位毫秒，0表示无线等待
cv2.waitKey(0)
# 释放内存空间，由于cv底层是c++，所以cv调用
cv2.destroyWindow()