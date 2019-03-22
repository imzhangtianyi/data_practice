import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope


class If:
    def __init__(self, data):
        self.df = data
        self.model = None

    def fit(self, contamination=.1, random_state=42):
        model = IsolationForest(contamination=contamination, random_state=random_state)
        model.fit(self.df)
        return model.predict(self.df)

class Lo:
    def __init__(self, data):
        self.df = data
        self.model = None

    def fit(self, contamination=.1):
        model = LocalOutlierFactor(contamination=contamination)
        return model.fit_predict(self.df)

class Svm:
    def __init__(self, data):
        self.df = data
        self.model = None

    def fit(self):
        model = OneClassSVM(kernel='linear')
        return model.fit_predict(self.df)

class Rc:
    def __init__(self, data):
        self.df = data
        self.model = None

    def fit(self, contamination=.1, random_state=42):
        model = EllipticEnvelope(contamination=contamination, random_state=random_state)
        return model.fit_predict(self.df)


if __name__ == "__main__":
    df = pd.read_csv('ship-data.csv')
    v = df[df.columns[11]].values
    u = df[df.columns[12]].values
    x = np.concatenate([v.reshape(-1, 1), u.reshape(-1, 1)], axis=1)
    prd = Rc(x).fit(.002)
    # prd = Lo(x).fit(contamination=.01)
    sns.scatterplot(df[df.columns[11]], df[df.columns[12]], hue=-prd)
    plt.show()
