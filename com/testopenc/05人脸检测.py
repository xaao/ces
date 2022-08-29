from cv2 import cv2 as cv
def face_detect_demo():
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #加载特征数据
    face_detector=cv.CascadeClassifier(r'D:\opncvfile\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')#模型
    # 对灰度图片进行识别，得出识别的画框数据x,y,w,h;;scaleFactor=1检测区域缩放比例为1;scaleFactor--表示在前后两次相继的扫描中，搜索窗口的比例系数。默认为1.1即每次搜索窗口依次扩大10%;
    # ,minNeighbors=3最少检测次数为3，minSize=2,maxSize框的大小;minSize和maxSize用来限制得到的目标区域的范围。
    faces=face_detector.detectMultiScale(gray,minNeighbors=12,minSize=(70,70))
    #循环特征数据
    for x,y,w,h in faces:
        # 利用特征数据画框
        print(x,y,w,h)
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=3)
        cv.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0),thickness=2)
    cv.imshow('huantu',img)
img=cv.imread('./images/duoren.jpg')
face_detect_demo()

cv.waitKey(0)
cv.destroyWindow()