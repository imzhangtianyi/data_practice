import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
sns.set(font_scale=1)
sns.set_style("whitegrid")
# sns.set_context("poster")
sns.set_style(rc={
    'axes.edgecolor': 'black',
    'axes.labelcolor': 'black',
    'xtick.bottom': True,
    'xtick.color': 'black',
    'ytick.left': True,
    'ytick.right': True,
    'ytick.color': 'black',
    'text.color': 'black',
    'text.size': '12',
    'font.sans-serif': ['DejaVu Sans',
                        'Liberation Sans',
                        'Bitstream Vera Sans',
                        'sans-serif'],
    })

class Lr:
    def __init__(self, x, y, size=0.2, random_state=42):
        self.xtr, self.xte, self.ytr, self.yte = train_test_split(x, y, test_size=size, random_state=random_state)
        self.model = None

    def fit(self):
        model = LogisticRegression()
        model.fit(self.xtr, self.ytr)
        self.model = model
        print('Train set accuracy:')
        print(model.score(self.xtr, self.ytr))
        print('Test set accuracy:')
        print(self.model.score(self.xte, self.yte))


class rf:
    def __init__(self, x, y, size=0.2, random_state=42):
        self.xtr, self.xte, self.ytr, self.yte = train_test_split(x, y, test_size=size, random_state=random_state)
        self.model = None

    def fit(self):
        model = RandomForestClassifier()
        model.fit(self.xtr, self.ytr)
        self.model = model
        print('Train set accuracy:')
        print(model.score(self.xtr, self.ytr))
        print('Test set accuracy:')
        print(self.model.score(self.xte, self.yte))


class Roc:
    def __init__(self, model, method='decision_function'):
        self.model = model
        self.method = method

    def plot(self, x, y, cv=5, fontsize=16):
        if self.method == 'decision_function':
            ys = cross_val_predict(self.model, x, y, cv=cv, method=self.method)
        elif self.method == 'predict_proba':
            ys = cross_val_predict(self.model, x, y, cv=cv, method=self.method)[:, 1]

        # ROC
        fpr, tpr, thr = roc_curve(y, ys)
        plt.plot(fpr, tpr)
        plt.plot([0, 1], [0, 1], '--')
        plt.axis([0, 1, 0, 1])
        plt.xlabel('1 - Specificity', fontsize=fontsize)
        plt.ylabel('Sensitivity', fontsize=fontsize)
        plt.show()
        # AUC
        print(roc_auc_score(y, ys))




if __name__ == "__main__":

