from cv2 import cv2
import numpy as np
import os
# 加载序列数据和文件,创建人脸识别对象
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('./trainer/trainer.yml')

#准备识别图片
img=cv2.imread('./images/xlz/xlz35.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_detector=cv2.CascadeClassifier(r'D:\opncvfile\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')#模型
# 对灰度图片进行识别，得出识别的画框数据x,y,w,h;;scaleFactor=1检测区域缩放比例为1;scaleFactor--表示在前后两次相继的扫描中，搜索窗口的比例系数。默认为1.1即每次搜索窗口依次扩大10%;
# ,minNeighbors=3最少检测次数为3，minSize=2,maxSize框的大小;minSize和maxSize用来限制得到的目标区域的范围。
faces=face_detector.detectMultiScale(gray,minNeighbors=12,minSize=(70,70))
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=3)
    id,condifence=recognizer.predict(gray[y:y+h,x:x+w])
    print(id,"置信评分：",condifence)
#     评分越高越不像，id是模型中训练的图形
cv2.imshow('huantu', img)
cv2.waitKey(0)
cv2.destroyWindow()