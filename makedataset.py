from PIL import Image
import numpy as np
import os


# 特征提取，获取图像二值化数学值
def getBinaryPix(im):
    im = Image.open(im)
    img = np.array(im)
    rows, cols = img.shape
    for i in range(rows):
        for j in range(cols):
            if img[i, j] <= 128:
                img[i, j] = 0
            else:
                img[i, j] = 1
    binpix = np.ravel(img)
    return binpix


def getfiles(f_dirs):
    fs = []
    for fr in os.listdir(f_dirs):
        f = f_dirs + fr
        # if f.rfind(u'.%s') == -1:
        fs.append(f)
    return fs


def writeFile(f_content):
    with open(u'train_data.txt', 'a+') as f:
        f.write(f_content)
        f.write('\n')
        f.close()


if __name__ == '__main__':
    dirs = u'category/%s/'
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(10):
        for f in getfiles(dirs % i):
            pixs = getBinaryPix(f).tolist()
            pixs.append(i+48)
            pixs = [str(i) for i in pixs]
            content = ','.join(pixs)
            writeFile(content)
    # k = 9
    # for i in s:
    #     k = k + 1
    #     for f in getfiles(dirs % i):
    #         pixs = getBinaryPix(f).tolist()
    #         pixs.append(k)
    #         pixs = [str(i) for i in pixs]
    #         content = ','.join(pixs)
    #         writeFile(content)

    for i in s:
        for f in getfiles(dirs % i):
            pixs = getBinaryPix(f).tolist()
            pixs.append(ord(i))
            pixs = [str(i) for i in pixs]
            content = ','.join(pixs)
            writeFile(content)