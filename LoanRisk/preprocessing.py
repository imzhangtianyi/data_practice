import pandas as pd
from functools import reduce

from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, ExtraTreesClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression, Lasso
from sklearn.model_selection import cross_val_score


class NA:
    def __init__(self, data: 'DataFrame'):
        self.df = data
        self.df_drop = data
        self.df_replace = data.copy()

    def to_num(self, category: 'str'):
        self.df[category] = pd.to_numeric(self.df[category], errors='coerce')
        self.df = self.df.sort_values(category)
        return self.df

    def drop(self, category: 'str'):
        """
        Drop rows with NaN in a column
        :param category: drop rows with NaN in this column
        :return: DataFrame with drop rows
        """
        df_drop = self.df.dropna(subset=[category])
        self.df_drop = self.df_drop.dropna(subset=[category])
        return df_drop

    def replace(self):
        """
        Replace instead drop rows
        :param category: Replace null with most common value
        :return: DataFrame with replaced values
        """
        columns = self.df.columns
        df = self.df_replace
        for c in columns:
            if df[c].dtype == 'O':
                df.loc[self.df_replace[c].isnull(), [c]] = df[c].value_counts().index[0]
            else:
                df.loc[self.df_replace[c].isnull(), [c]] = df[c].median()
        self.df_replace = df
        return df


class Merge:
    def __init__(self, data: 'DataFrames'):
        self.data = data

    def transform(self, on: 'str'):
        """
        Merge all dataframe on a column
        :param on: column name
        :return: Dataframe
        """
        df_merge = reduce(lambda left, right: pd.merge(left, right, on=[on], how='outer'), self.data)
        df_merge = df_merge.sort_values(on)
        return df_merge


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
        Ordinal encoding for all non-numerical columns
        """
        columns = data.columns
        for c in columns:
            if data[c].dtype == 'O':
                enc = LabelEncoder()
                data[c] = enc.fit_transform(data[c])
        return data

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

    def rf(self, max_depth=None, n=10):
        model = RandomForestClassifier(max_depth=max_depth, n_estimators=n, n_jobs=-1)
        model.fit(self.xtr, self.ytr)
        print("train accuracy:")
        print(model.score(self.xtr, self.ytr))
        print("cv accuracy:")
        print(cross_val_score(model, self.xtr, self.ytr, cv=5))
        self.yimpute = model.predict(self.ximpute)

    def et(self):
        model = ExtraTreesClassifier()
        model.fit(self.xtr, self.ytr)
        print("train accuracy:")
        print(model.score(self.xtr, self.ytr))
        print("cv accuracy:")
        print(cross_val_score(model, self.xtr, self.ytr, cv=5))
        self.yimpute = model.predict(self.ximpute)

    def rf_reg(self):
        model = RandomForestRegressor()
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

    def lasso(self):
        model = Lasso()
        model.fit(self.xtr, self.ytr)
        print("train accuracy:")
        print(model.score(self.xtr, self.ytr))
        print("cv accuracy:")
        print(cross_val_score(model, self.xtr, self.ytr, cv=5))
        self.yimpute = model.predict(self.ximpute)


if __name__ == '__main__':
    column_credit = ['CustomerID', 'CheckingAccountBalance', 'DebtsPaid', 'SavingsAccountBalance',
                     'CurrentOpenLoanApplications']
    df_credit = pd.read_csv('ds-credit.tsv', sep='\s+', header=-1, names=column_credit)

    column_app = ['CustomerID', 'LoanPayoffPeriodInMonths', 'LoanReason', 'RequestedAmount', 'InterestRate',
                  'Co-Applicant']
    df_app = pd.read_csv('ds-app.tsv', sep='\s+', header=-1, names=column_app)

    column_borrower = ['CustomerID', 'YearsAtCurrentEmployer', 'YearsInCurrentResidence', 'Age', 'RentOrOwnHome',
                       'TypeOfCurrentEmployment', 'NumberOfDependantsIncludingSelf']
    df_borrower = pd.read_csv('ds-borrower.csv', sep='\s+', index_col=False, names=column_borrower, header=0)

    column_result = ['CustomerID', 'WasTheLoanApproved']
    df_result = pd.read_csv('ds-result.tsv', sep='\s+', header=-1, names=column_result)
    df_result = df_result.drop_duplicates()  # Drop the duplicated results

    na = NA(df_borrower)
    na.to_num('CustomerID')
    df_borrower = na.drop('CustomerID')

    na = NA(df_result)
    na.to_num('CustomerID')
    df_result = na.drop('CustomerID')

    mg = Merge([df_credit, df_app, df_borrower, df_result])
    d = mg.transform('CustomerID')
    print(Encode().ordinal(d))

