English | [简体中文](/README.zh.md)
# Introduction
A small program for downloading [douyin](https://www.douyin.com/) short videos (without watermark) , which is made with Python.
# Demo
![demo.gif](/demo.gif)
# Install
```bash
pip install requests tqdm
```
# Usage
1. Git clone adn run `down.py`.
```bash
git clone https://github.com/XavierJiezou/python-dy-down.git
cd python-dy-down
python down.py
```
2. Input a video url from [douyin](https://www.douyin.com/), like: [https://v.douyin.com/JVFp8r5/](https://v.douyin.com/JVFp8r5/).
```bash
请输入复制的快手分享链接：https://v.douyin.com/JVFp8r5/
正在请求，预计需要3秒：
100%|█████████████| 6/6 [00:00<00:00, 1983.12KB/s]
下载完成，总计用时3秒。
```
3. [6904393356240047368.mp4](6904393356240047368.mp4) is the video that just downloaded.
# Unpack
```bash
git clone https://github.com/XavierJiezou/python-dy-down.git
cd python-dy-down
pipenv install
pipenv shell
pip install requests tqdm
pip install pyinstaller
pyinstaller -F -i favicon.ico down.py
```
---
Note: Building EXE is placed in the `dist` folder.
# Download
> [ksdown-1.0.0-win64.exe](https://github.com/XavierJiezou/python-ks-down/releases/download/1.0.0/ksdown-1.0.0-win64.exe)
# Recommend
> [python-dy-down](https://github.com/XavierJiezou/python-ks-down): A small program for downloading [duouyin](https://www.douyin.com/) short videos.
