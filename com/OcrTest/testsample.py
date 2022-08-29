import os
import random
from captcha.image import ImageCaptcha
def zifuchuan():
    a=random.sample("zxvcbnm", 1)+random.sample("zxvcbnm", 1)+random.sample("zxvcbnm", 1)+random.sample("zxvcbnm", 1)
    return a
def generamulu(save_path,a):
    image=ImageCaptcha()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    image.write(a,'%s/%s.png'%(save_path, a))
    return save_path


if __name__ == '__main__':
    a=zifuchuan()