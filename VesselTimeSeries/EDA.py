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


class Info:
    def __init__(self, data: 'DataFrame'):
        self.df = data

    def categories(self):
        """
        Print information for each column: 5 examples, data type, number of unique data
        :return: None
        """
        col = self.df.columns
        for i in col:
            print('\n' + i + ':')
            print(self.df[i].unique()[:5])
            print(self.df[i].dtype)
            print(self.df[i].unique().shape)

    def duplicate(self):
        """
        Check duplicate
        :return: None
        """
        df_duplicate = self.df.drop_duplicates()
        print('df:')
        print(self.df.shape)
        print('Remove duplicate:')
        print(df_duplicate.shape)

    def missing(self, bar: 'bool' = False) -> 'None':
        """
        Show missing values
        :param bar: show missing values in a bar graph
        :return: None
        """
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
        self.df = data  # NaN data removed
        self.figsize = (15, 4)

    def set_size(self, m: 'int', n: 'int'):
        """
        Set figure size
        :param m: horizontal
        :param n: vertical
        :return: None
        """
        self.figsize = (m, n)

    def plot(self, category: 'str', fontsize=20, xlabel='Hour'):
        """
        Plot the time series
        """
        plt.figure(figsize=self.figsize)
        plt.plot(self.df[category])
        plt.xlabel(xlabel, fontsize=fontsize)
        plt.title(category, fontsize=fontsize)
        plt.tight_layout()
        plt.show()
        print(self.df[category].describe())

    def correlation(self, vmax=1, vmin=-1, center=0, rotation=30, fontsize=10):
        """
        Plot the pearson correlation between each categories
        """
        df = self.df.corr()

        mask = np.zeros_like(df, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        plt.figure(figsize=self.figsize)
        cmap = sns.diverging_palette(220, 10, as_cmap=True)

        corr = sns.heatmap(df, mask=mask, cmap=cmap, vmax=vmax, vmin=vmin, center=center,
                    square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, annot_kws={'fontsize':fontsize})
        corr.set_xticklabels(corr.get_xticklabels(), rotation=rotation, fontsize=fontsize)
        plt.show()




if __name__ == '__main__':
    df = pd.read_csv('ship-data.csv')
    # Visual(df).plot('Main Engine Fuel Consumption (MT/day)')
    Visual(df).correlation()