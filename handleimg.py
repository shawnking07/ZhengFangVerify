from PIL import Image, ImageEnhance, ImageFilter
import time
import os


# 利用crop将图片裁成四块
def segment(im):
    s = 5
    w = 12
    h = 24
    t = 0
    im_new = []
    for i in range(4):

        im1 = im.crop((s + w * i, t, s + w * (i + 1), h))
        # im.crop剪裁图片
        im_new.append(im1)
    return im_new


# 图片预处理，二进制化，图片增强
def imgTransfer(f_name):
    im = Image.open(f_name)
    im = im.filter(ImageFilter.MedianFilter())
    # 滤镜medianfilter是中值滤波器作用是减少噪声
    im = im.convert('L')
    # convert图像模式转换转为Ｌ模式 笔记：PIL库共有９种模式
    return im


def cutPictrues(img):
    im = imgTransfer(img)
    pics = segment(im)
    for pic in pics:
        pic.save(u'num/%s.jpg' % (int(time.time() * 1000000)), 'jpeg')


def getAllImages(folder):
    assert os.path.exists(folder)
    assert os.path.isdir(folder)
    # 断言assert判断路径是否存在与路径是否为目录
    imageList = os.listdir(folder)
    # os.listdir获取指定路径下的内容
    imageList = [os.path.abspath(item) for item in imageList if os.path.isfile(os.path.join(folder, item))]
    return imageList


# if __name__ == '__main__':
#     files_name = getAllImages(u'pics//')
#     for i in files_name:
#         files = i.replace('\\', '/')
#         s = files.split('/')
#         name = ''
#         for j in s[:-1]:
#             name = name + j + '/'
#         name = name + 'pics/' + s[-1]
#         print(name)
#         cutPictrues(name)
