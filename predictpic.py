from makedataset import *
from handleimg import *
from sklearn.externals import joblib
import os


def cutPic(name):
    im = imgTransfer(name)
    pics = segment(im)
    i = 1
    for pic in pics:
        pic.save(u'test_picture/%s.jpg' % i, 'jpeg')
        i = i + 1


def load_Predict(name):
    cutPic(name)  # 切割图片

    dirs = u'test_picture/'
    fs = os.listdir(dirs)  # 获取图片名称
    clf = joblib.load("train_model.m")
    predictValue = []

    for fname in fs:
        fn = dirs + fname
        binpix = getBinaryPix(fn).reshape(1, -1)
        predictValue.append(clf.predict(binpix))

    predictValue = [str(chr(i)) for i in predictValue]
    print("the picture number is :", "".join(predictValue))


if __name__ == '__main__':
    for i in range(5):
        load_Predict("test" + str(i) + ".jpeg")
