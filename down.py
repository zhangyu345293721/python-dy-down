import os
import re
import json
import requests
from tqdm import tqdm


def down():
    inp = input('请输入复制的抖音分享链接：')  # 如：https://v.douyin.com/JV2WKMu/
    url = re.findall('https://v.douyin.com/.*?/', inp)[0]  # 链接解析
    res = requests.get(url)
    vid = re.findall('/video/(.*?)/', res.url)[0]  # vid解析，vid就是视频id，是我自己定义的
    api = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={vid}' # 调用api
    res = requests.get(api).json()
    url = res['item_list'][0]['video']['play_addr']['url_list'][0]  # 视频下载链接解析
    url = url.replace('/playwm/', '/play/')  # 去水印
    res = requests.get(url, headers={'user-agent': 'chrome'})
    total_size = round(int(res.headers["Content-Length"])/1024/1024)
    with open(f'{vid}.mp4', 'wb') as f:
        for chunk in tqdm(iterable=res.iter_content(1024*1024), total=total_size, unit='KB', ncols=50):
            f.write(chunk)
    os.system('pause')


if __name__ == '__main__':
    down()
