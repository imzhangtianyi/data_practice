import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, f1_score
import matplotlib.pyplot as plt


class Data:
    def __init__(self):
        self.iris = load_iris()
        self.x = self.iris.data
        self.y = self.iris.target

    def transform(self, category: 'int' = 0, split: 'float' = .2):
        y = map(lambda x: 1 if x == category else 0, self.y)
        y = list(y)
        y = np.array(y)
        n = len(y)
        perm = np.random.permutation(n)
        i = int(100 * split)
        xtr, xte = self.x[perm][i:], self.x[perm][:i]
        ytr, yte = y[perm][i:], y[perm][:i]
        return xtr, xte, ytr, yte


class Logistic:
    def __init__(self, learning_rate: 'float' = 0.01):
        self.learning_rate = learning_rate
        self.W = np.zeros((4, 1))
        self.b = np.zeros((1, 1))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def loss(self, y, y_hat):
        return -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))

    def train(self, xtr, ytr, epoch: 'int' = 5000, p: 'float' = 0.5):
        m = len(ytr)
        ytr = ytr.reshape(-1, 1)
        w = self.W
        b = self.b

        for e in range(epoch):
            wx = np.matmul(xtr, w) + b
            h = self.sigmoid(wx)
            l = self.loss(ytr, h)
            dz = wx - ytr
            dw = np.matmul(xtr.T, dz) / m
            db = sum(dz)

            w = w - dw * self.learning_rate
            b = b - db * self.learning_rate

            if e % 100 == 0:
                print(l)
        self.W = w
        self.b = b
        prd = []
        for i in h:
            if i > p:
                prd.append(1)
            else:
                prd.append(0)
        print('\naccuracy:')
        print(accuracy_score(ytr, prd))
        print('\nf1:')
        print(f1_score(ytr, prd))

    def predict(self, x, p: 'float' = 0.5):
        prd = []
        wx = np.matmul(x, self.W) + self.b
        h = self.sigmoid(wx)
        for i in h:
            if i > p:
                prd.append(1)
            else:
                prd.append(0)
        return prd


if __name__ == "__main__":
    xtr, xte, ytr, yte = Data().transform()
    Logistic().train(xtr, ytr)
