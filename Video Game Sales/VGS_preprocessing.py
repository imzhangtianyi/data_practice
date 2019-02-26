import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split


class NA:
    def __init__(self, data: 'DataFrame'):
        self.df = data
        self.df_drop = data
        self.df_replace = data

    def drop(self, category: 'str'):
        df_drop = self.df.dropna(subset=[category])
        self.df_drop = self.df_drop.dropna(subset=[category])
        return df_drop

    def replace(self, category: 'str'):
        self.df_replace.loc[self.df_replace[category].isnull(), [category]] = '_missing_'
        return self.df_replace


class Impute:
    def __init__(self, data: 'DataFrame'):
        self.df = data
        self.df_impute = data
        self.train = None
        self.predict = None
        self.xtr = None
        self.ytr = None
        self.ximpute = None
        self.yimpute = None

    def set_train(self, y: 'str' = 'Year', col=['Platform', 'Genre']):
        self.train = self.df.loc[self.df[y].notnull()]
        self.predict = self.df.loc[self.df[y].isnull()]
        self.xtr = self.train[col]
        self.ytr = self.train[y]
        self.ximpute = self.predict[col]

    def impute(self, y: 'str' = 'Year'):
        self.df_impute.loc[self.df[y].isnull(), [y]] = self.yimpute

    def knn(self, k: 'int' = 5):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(self.xtr, self.ytr)
        print("train accuracy:")
        print(model.score(self.xtr, self.ytr))
        print("cv accuracy:")
        print(cross_val_score(model, self.xtr, self.ytr, cv=5))
        self.yimpute = model.predict(self.ximpute)

    def rf(self):
        model = RandomForestClassifier()
        model.fit(self.xtr, self.ytr)
        print("train accuracy:")
        print(model.score(self.xtr, self.ytr))
        print("cv accuracy:")
        print(cross_val_score(model, self.xtr, self.ytr, cv=5))
        self.yimpute = model.predict(self.ximpute)

    def nb(self):
        model = MultinomialNB()
        model.fit(self.xtr, self.ytr)
        print("train accuracy:")
        print(model.score(self.xtr, self.ytr))
        print("cv accuracy:")
        print(cross_val_score(model, self.xtr, self.ytr, cv=5))
        self.yimpute = model.predict(self.ximpute)

    def lr(self):
        model = LogisticRegression()
        model.fit(self.xtr, self.ytr)
        print("train accuracy:")
        print(model.score(self.xtr, self.ytr))
        print("cv accuracy:")
        print(cross_val_score(model, self.xtr, self.ytr, cv=5))
        self.yimpute = model.predict(self.ximpute)


class Encode:
    def __init__(self):
        self.encoder = None

    def one_hot(self, data):
        enc = OneHotEncoder(handle_unknown="ignore")
        enc.fit(data)
        self.encoder = enc


if __name__ == '__main__':
    filename = "vgsales.csv"
    df = pd.read_csv(filename)
    dn = NA(df)
    # df1 = dn.drop('Year')
    df1 = dn.replace('Publisher')
    impute = Impute(df1)
    impute.set_train(col=['Platform', 'Genre', 'Publisher'])
    # impute.train
    # print(impute.xtr.head().values)
    en = Encode()
    en.one_hot(impute.xtr)
    impute.xtr = en.encoder.transform(impute.xtr)
    impute.ximpute = en.encoder.transform(impute.ximpute)
    impute.nb()
    impute.impute()
    import EDA
    EDA.Info(impute.df_impute).missing()

