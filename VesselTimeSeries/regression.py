import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor

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
        model = LinearRegression()
        model.fit(self.xtr, self.ytr)
        self.model = model
        print('Train set accuracy:')
        print(model.score(self.xtr, self.ytr))
        print('Test set accuracy:')
        print(self.model.score(self.xte, self.yte))


class Rr:
    def __init__(self, x, y, size=0.2, random_state=42):
        self.xtr, self.xte, self.ytr, self.yte = train_test_split(x, y, test_size=size, random_state=random_state)
        self.model = None

    def fit(self, alpha=1, random_state=42):
        model = Ridge(alpha=alpha, random_state=random_state)
        model.fit(self.xtr, self.ytr)
        self.model = model
        print('Train set accuracy:')
        print(model.score(self.xtr, self.ytr))
        print('Test set accuracy:')
        print(self.model.score(self.xte, self.yte))

    def grid_search(self, param={'alpha':[.1, 1, 10]}, cv=5):
        model = Ridge(random_state=42)
        grid = GridSearchCV(model, param, cv=cv)
        grid.fit(self.xtr, self.ytr)
        print(grid.cv_results_['params'])
        print(grid.cv_results_['mean_test_score'])


class Ls:
    def __init__(self, x, y, size=0.2, random_state=42):
        self.xtr, self.xte, self.ytr, self.yte = train_test_split(x, y, test_size=size, random_state=random_state)
        self.model = None

    def fit(self, alpha=1, random_state=42):
        model = Lasso(alpha=alpha, random_state=random_state)
        model.fit(self.xtr, self.ytr)
        self.model = model
        print('Train set accuracy:')
        print(model.score(self.xtr, self.ytr))
        print('Test set accuracy:')
        print(self.model.score(self.xte, self.yte))

    def grid_search(self, param={'alpha':[.1, 1, 10]}, cv=5):
        model = Ridge(random_state=42)
        grid = GridSearchCV(model, param, cv=cv)
        grid.fit(self.xtr, self.ytr)
        print(grid.cv_results_['params'])
        print(grid.cv_results_['mean_test_score'])


class Rf:
    def __init__(self, x, y, size=0.2, random_state=42):
        self.xtr, self.xte, self.ytr, self.yte = train_test_split(x, y, test_size=size, random_state=random_state)
        self.model = None

    def fit(self):
        model = RandomForestRegressor()
        model.fit(self.xtr, self.ytr)
        self.model = model
        print('Train set accuracy:')
        print(model.score(self.xtr, self.ytr))
        print('Test set accuracy:')
        print(self.model.score(self.xte, self.yte))


if __name__ == "__main__":
    df = pd.read_csv('ship-data.csv')
    x = df['Speed Through Water (knots)'].values.reshape(-1, 1)
    y = df['Main Engine Fuel Consumption (MT/day)'].values.reshape(-1, 1)
    lr = Rr(x, y)
    lr.grid_search()