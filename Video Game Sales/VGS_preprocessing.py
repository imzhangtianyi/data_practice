import pandas as pd

from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score


class NA:
    def __init__(self, data: 'DataFrame'):
        self.df = data
        self.df_drop = data
        self.df_replace = data.copy()

    def drop(self, category: 'str'):
        """
        Drop rows with NaN in a column
        :param category: drop rows with NaN in this column
        :return: DataFrame with drop rows
        """
        df_drop = self.df.dropna(subset=[category])
        self.df_drop = self.df_drop.dropna(subset=[category])
        return df_drop

    def replace(self, category: 'str'):
        """
        Replace instead drop rows
        :param category: Replace NaN with '_missing_' in this column
        :return: DataFrame with replaced values
        """
        self.df_replace.loc[self.df_replace[category].isnull(), [category]] = '_missing_'
        return self.df_replace


class Impute:
    def __init__(self, data: 'DataFrame'):
        self.df = data
        self.df_impute = data.copy()
        self.train = None
        self.predict = None
        self.xtr = None
        self.ytr = None
        self.ximpute = None
        self.yimpute = None

    def set_train(self, y: 'str', col: 'List'):
        df = self.df.copy()
        self.train = df.loc[self.df[y].notnull()]
        self.predict = df.loc[self.df[y].isnull()]
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
        """
        One-hot encoding without intercept. Two or more features will generate a co-linear dependency.
        """
        enc = OneHotEncoder(handle_unknown="ignore")
        enc.fit(data)
        self.encoder = enc

    def ordinal(self, data):
        """
        Ordinal encoding. Does not work for multiple columns
        """
        enc = LabelEncoder()
        enc.fit(data)
        self.encoder = enc

    def tfidf(self, data):
        


if __name__ == '__main__':
    filename = "vgsales.csv"
    df = pd.read_csv(filename)
    dn = NA(df)
    # df1 = dn.drop('Year')
    df1 = dn.replace('Publisher')
    impute = Impute(df1)
    impute.set_train()
    # impute.train
    # print(impute.xtr.head().values)
    en = Encode()
    en.ordinal(impute.xtr)
    print(impute.xtr.columns)
    print(impute.xtr.Platform.unique().shape)
    print(impute.xtr.Genre.unique().shape)
    print(en.encoder.transform(impute.xtr.Genre).shape)

