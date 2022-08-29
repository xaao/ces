from cv2 import cv2

# 读取图片
image=cv2.imread(r'./images/7921.png')#图片路径不能为中文
# 显示图片
cv2.imshow('input_image',image)
print('之前图片形状',image.shape)
# 修改尺寸
resize_img=cv2.resize(image,dsize=(300,340))
cv2.imshow('resize_img',resize_img)

print('之后图片形状',resize_img.shape)
# 等待键盘输入，单位毫秒，0表示无线等待

while True:
    if ord("q") == cv2.waitKey(0):
        break
# 释放内存空间，由于cv底层是c++，所以cv调用
cv2.destroyWindow()