import cv2 as cv

img=cv.imread(r'./images/img.png')
x,y,w,h=30,30,20,20
# 绘制矩形
# cv.rectangle(img,(x,y,x+w,y+h),color=(0,255,0),thickness=3)
# cv.imshow('huatu_img',img)
# 绘制圆,raduis半径
x1,y1,r=60,50,30
cv.circle(img,center=(x1,y1),radius=r,color=(0,0,255),thickness=2)
cv.imshow('huatu_img',img)
cv.waitKey(0)
cv.destroyWindow()