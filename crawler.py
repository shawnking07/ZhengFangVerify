# -*- coding:utf-8 -*-
import requests
import time

from PIL import Image


def download_pics(pic_name):
    url = 'http://10.80.96.131/CheckCode.aspx'
    res = requests.get(url, stream=True)
    # stream=True代表想获取来自服务器的原始嵌套字相应
    with open(u'cache/%s.png' % (pic_name), 'wb')as f:
        # wb以二进制写模式打开
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()


if __name__ == '__main__':
    for i in range(2):
        pic_name = int(time.time() * 1000000)
        download_pics(pic_name)
        name = u'cache/' + str(pic_name) + '.png'
        im = Image.open(name)
        im = im.convert('RGB')
        nname = u'tests/' + str(pic_name) + '.jpeg'
        im.save(nname, "jpeg")

