import threading
import requests

# a=[15,16,17,18,19,20,21,22]
# for i in range(len(a)):
#     video_list=["20{}年电影".format(a[i]),'https://vip.1905.com/list/t_2_y_20{}/p1o6.shtml'.format(a[i])]


re=requests.get('https://www.1905.com/vod/play/85676.shtml').content
with open('./img/223.mp4','wb') as f:
    f.write(re)

