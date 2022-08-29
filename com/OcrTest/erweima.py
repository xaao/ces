import os
import random  # 生成随机验证码
from captcha.image import ImageCaptcha  # 生成图片
import time

def number():   # 生成随机验证码字符串
    # captcha_text = [str(i) for i in range(10)]   # 列表形式纯数字，列表的内容为字符串形式的0-9
    captcha_text = '0123456789' #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    example = [random.sample(captcha_text, 1)[0] for i in range(4)] #生成一个列表,四个随机字符
    verification_code = ''.join(example)   # 将4个字符拼接
    return verification_code   # 返回验证码内容

def generate_captcha_image(save_path,number):    # 生成验证码图片
    image = ImageCaptcha()
    if not os.path.exists(save_path):   # 检测目录是否存在，不在则创建
        os.makedirs(save_path)
    image.write(number, '%s/%s.png'%(save_path, number))   # 保存图片
    return save_path   # 返回保存文件的文件夹，方便后期删除

def remove(path):   # 退出程序的时候一定要记得删除验证码，否则内存占用会越来越大
    files=os.listdir(path) # 获取目录下的文件
    os.chdir(path)  # 进入目录
    for file in files:os.remove(file)  #遍历删除指定目录下的文件
    os.chdir("..")  # 返回当前目录
    os.rmdir(path)    # 删除这个目录，可根据需要保存这个目录
    return

if __name__ == "__main__":
    nb = number()
    print(nb)
    image = generate_captcha_image("images",nb)  # 生成验证码，第一个参数为保存的路径
    print("验证码保存在：",image)
