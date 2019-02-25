import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import missingno as msno
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
# sns.set_palette('Set2')


class Info:
    def __init__(self, filename: 'str'):
        self.df = pd.read_csv(filename)

    def categories(self, ncolums: 'int' = 5):
        col = self.df.columns[:ncolums]
        for i in col:
            print('\n' + i + ':')
            print(self.df[i].unique()[:5])
            print(self.df[i].dtype)
            print(self.df[i].unique().shape)

    def duplicate(self):
        self.df_duplicate = self.df.drop_duplicates()
        print('df:')
        print(self.df.shape)
        print('Remove duplicate:')
        print(self.df_duplicate.shape)

    def missing(self, bar: 'bool' = False) -> 'None':
        col = self.df.columns
        for i in col:
            mis = self.df[i].isnull()
            if mis.any():
                print('\n' + i + ':')
                print(self.df[i].isnull().sum()/self.df.shape[0])
        if bar:
            msno.bar(self.df)
            plt.show()
        else:
            msno.matrix(self.df)
            plt.show()


class Visual:
    def __init__(self, data: 'DataFrame'):
        self.df = data.loc[data.isnull().sum(1).apply(lambda x: not x)]  # NaN data removed
        self.figsize = (14, 8)

    def set_size(self, m: 'int', n: 'int'):
        self.figsize = (m, n)

    def annual_sale(self, sub: 'bool' = True, avg: 'bool' = False):
        df = self.df
        regions = df.columns[6:]
        if sub:
            fig, ax = plt.subplots(2, 3, figsize=self.figsize)

            for reg, a in zip(regions, ax.ravel()):
                if not avg:
                    sales = df.groupby('Year')[reg].sum()
                else:
                    sales = df.groupby('Year')[reg].mean()
                a.plot(sales)
                a.set_title(reg)
            fig.delaxes(ax.ravel()[-1])
        else:
            plt.figure(figsize=self.figsize)
            for reg in regions:
                if not avg:
                    sales = df.groupby('Year')[reg].sum()
                else:
                    sales = df.groupby('Year')[reg].mean()
                plt.plot(sales, label=reg)
            plt.ylabel('Sales [million]')
            plt.legend()
        plt.show()

    def annual_games(self):
        df = self.df
        plt.figure(figsize=self.figsize)
        bar = sns.countplot(df.Year)
        bar.set_xticklabels(bar.get_xticklabels(), rotation=40, fontsize=10)
        plt.show()

    def avg_sale(self, category: 'column', top: 'int' = 10):
        df = self.df
        regions = df.columns[6:]
        fig, ax = plt.subplots(2, 3, figsize=self.figsize)
        for reg, a in zip(regions, ax.ravel()):
            sale = df.groupby(category)[reg].mean()
            sale = sale.sort_values(ascending=False)[:top]
            bar = sns.barplot(sale.index, sale, ax=a)
            bar.set_xticklabels(sale.index, rotation=40, fontsize=10)
            a.set_title(reg)
        fig.delaxes(ax.ravel()[-1])
        plt.show()

    def hist(self, region: 'str', bins: 'int' = 30, log: 'bool' = False):
        arr = self.df[region]
        if not log:
            sns.distplot(arr, bins=bins, hist_kws={'linewidth': 1})
        else:
            arr = np.log(arr)
            sns.distplot(arr, bins=bins, hist_kws={'linewidth': 1})
            plt.xlabel('Log ' + region)
        plt.show()


if __name__ == '__main__':
    filename = "vgsales.csv"
    df = pd.read_csv(filename)
    eda = Info(filename)
    # print(eda.df.head())
    # print(eda.df.shape)
    # print(eda.df.Name.value_counts()[:5])
    # print(eda.df.loc[eda.df.Name == 'Ratatouille'])
    # print(eda.df.Year.value_counts())
    # print(eda.df.Global_Sales.describe())
    # print(eda.df.Year.describe())
    # eda.categories()
    # print(df.head())
    # print(df.head())
    vs = Visual(df)
    # vs.avg_sale('Genre')
    # vs.annual_sale(False, True)
    # vs.annual_games()
    # eda.missing()
    vs.hist('Global_Sales', log=True)
