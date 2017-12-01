import warnings

from sklearn import cross_validation as cs
from sklearn import grid_search
from sklearn.externals import joblib
from sklearn.svm import SVC

from makedataset import *

warnings.filterwarnings('ignore')


def load_data():
    data = np.loadtxt(u'train_data.txt', delimiter=',')
    # print(data)
    return data


# 交叉验证
def cross_validation():
    dataset = load_data()
    row, col = dataset.shape
    X = dataset[:, :col - 1]
    Y = dataset[:, -1]
    clf = SVC(kernel='rbf', C=1000)
    clf.fit(X, Y)
    scores = cs.cross_val_score(clf, X, Y, cv=5)
    joblib.dump(clf, "train_model.m")
    print("Accuracy: %0.2f (+- %0.2f)" % (scores.mean(), scores.std()))
    # return clf


def searchBestParameter():
    parameters = {'kernel': ('linear', 'poly', 'rbf', 'sigmoid'), 'C': [1, 100]}
    dataset = load_data()
    row, col = dataset.shape
    X = dataset[:, :col - 1]
    Y = dataset[:, -1]
    svr = SVC()
    clf = grid_search.GridSearchCV(svr, parameters)
    clf.fit(X, Y)
    print(clf.best_params_)


def train():
    dataset = load_data()
    row, col = dataset.shape
    X = dataset[:, :col - 1]
    Y = dataset[:, -1]
    clf = SVC(kernel='rbf', C=1000)
    clf.fit(X, Y)
    joblib.dump(clf, "train_model.m")



if __name__ == '__main__':
    cross_validation()
    # train()
    # searchBestParameter()

