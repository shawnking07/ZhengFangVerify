from pytesseract import *
from PIL import Image
import os
import shutil


def ocr(img):
    try:
        img = Image.open(img)
        rs = image_to_string(img, config="-psm 10", lang="eng")
    except:
        return 'none'
    return rs


# 使用ocr进行训练的预分类
def category(originfile, dirs, filename):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    shutil.copyfile(originfile, dirs + filename)


# if __name__ == '__main__':
#     dirs = os.path.abspath(u'num') + '/'
#     # 将ocr识别的文件按照数组编号存放在相应的文件夹中
#     for fr in os.listdir(dirs):
#         f = dirs + fr
#         # 判断f是可以使用的
#         # if f.rfind(u'.%s') == -1:
#         rs = ocr(f)
#         if len(rs) == 1:
#             if rs.isalpha() and rs.islower():
#                 category(f, u'category/%s/' % rs, fr)
#             elif rs.isdigit():
#                 category(f, u'category/%s/' % rs, fr)
