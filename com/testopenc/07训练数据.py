import os
from cv2 import cv2
from PIL import Image
import numpy as np

def getImagesAndLables(path):
    faceSample=[]
    ids=[]
    imagesPaths=[os.path.join(path,f) for f in os.listdir(path)]
    face_detector = cv2.CascadeClassifier(
        r'D:\opncvfile\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')  # 模型
    for imagesPath in imagesPaths:
        # 打开图片
        PIL_img=Image.open(imagesPath).convert('L')
        #将图像转换为数组
        img_numpy=np.array(PIL_img,'uint8')
        id=os.path.split(imagesPath)[1].split('.')[0]
        faces = face_detector.detectMultiScale(img_numpy)
        for x,y,w,h in faces:
            faceSample.append(img_numpy[y:y+h,x:x+w])
            # 此处的id是字符串
            ids.append(int(id))
    # print(imagesPaths)
    return faceSample,ids
if __name__ == '__main__':
    #获取图像数组何id标签数据
    path='./images/images_lcw_xlz/'
    faces,ids=getImagesAndLables(path)
    print(ids)
    # 获取序列对象
    reconizer=cv2.face.LBPHFaceRecognizer_create()

    reconizer.train(faces,np.array(ids))
    # 保存文件
    reconizer.write('./trainer/trainer.yml')
