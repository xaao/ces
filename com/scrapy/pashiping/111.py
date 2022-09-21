import time
import requests
from tqdm import tqdm as tqdm

def getname():
    return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
def paqu(url,num):
    headers={'User-Agent':'Mozilla/ 5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/105.0.0.0 Safari/537.36'}
    conet=requests.get(url=url,headers=headers).json()
    # print(conet['data'][0]['playCnt'],conet['data'][0]['playUrl'])
    # print(conet)
    for i in range(num):
        # print(conet['data'][i]['playUrl'],conet['data'][i]['playCnt'])
        content_type=conet['data'][i]['playCnt']
        file_name=conet['data'][i]['title']
        b=requests.get(url=conet['data'][i]['playUrl'],headers=headers)
        # print(type(b))
        with open(f'./{getname()}.mp4','wb') as f,tqdm(
            desc=file_name,
            total=content_type,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
            colour='red',
        ) as bar:
            for data in b.iter_content(chunk_size=1024):
                size=f.write(data)
                bar.update(size)

if __name__ == '__main__':
    num=int(input("请输入要爬取几个视频："))
    url=f'https://www.ku6.com/video/feed?pageNo=0&pageSize={num}&subjectId=76'
    paqu(url,num)