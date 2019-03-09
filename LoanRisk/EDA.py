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
        self.df = data.loc[data.isnull().sum(1).apply(lambda x: not x)]  # NaN data removed
        self.figsize = (14, 8)

    def set_size(self, m: 'int', n: 'int'):
        """
        Set figure size
        :param m: horizontal
        :param n: vertical
        :return: None
        """
        self.figsize = (m, n)

    def percentage(self, category: 'str', rotation=0, fontsize=20):
        """
        Plot the percentage of each class in a category
        """
        df = self.df[category].value_counts()
        df = df.apply(lambda x: x/df.sum()*100)
        plt.figure(figsize=self.figsize)
        bar = sns.barplot(df.index, df, order=df.index)
        bar.set_xticklabels(bar.get_xticklabels(), rotation=rotation, fontsize=fontsize)
        plt.ylabel(category+' (Percentage)', fontsize=fontsize)
        plt.show()

    def hist(self, category: 'str', bins: 'int' = 30, log: 'bool' = False):
        """
        Plot a histogram for a category
        """
        arr = self.df[category]
        plt.figure(figsize=self.figsize)
        if not log:
            sns.distplot(arr, bins=bins, hist_kws={'linewidth': 1})
        else:
            arr = np.log(arr + 0.000001)
            sns.distplot(arr, bins=bins, hist_kws={'linewidth': 1})
            plt.xlabel('Log ' + category)
        plt.show()
        print(arr.describe())

    def correlation(self, vmax=.3, vmin=0, center=0.1, rotation=30, fontsize=12):
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

    def dist(self, x: 'str', y: 'str', bins: 'int' = 20):
        """
        Compare distribution
        :param x: category to compare
        :param y: on condition of this target variable
        """
        df_x = pd.to_numeric(self.df[x], errors='coerce')
        df_y = self.df[y]
        classes = df_y.unique()
        plt.figure(figsize=self.figsize)
        for c in classes:
            sns.distplot(df_x[df_y == c], bins=bins, label=c)
        plt.legend()
        plt.show()

    def compare(self, x: 'str', y: 'str', width=.2):
        """
        Compare percentage
        :param x: percentage to compare
        :param y: on condition of this target variable
        """
        df_x = self.df[x]
        df_y = self.df[y]
        y = df_y.unique()

        df = df_x[df_y==y[0]].value_counts()
        df = df.apply(lambda x: x/df.sum())
        df.name = y[0]
        df = pd.DataFrame(df)

        for c in y[1:]:
            x = df_x[df_y==c].value_counts()
            x = x.apply(lambda s: s/x.sum())
            x.name = c
            df = df.join(x)

        fig = df.plot(kind='bar', width=width, alpha=1, figsize=self.figsize)
        fig.set_xticklabels(df.index, rotation=40, fontsize=10)
        plt.legend()
        plt.show()




if __name__ == '__main__':
    # column_credit = ['CustomerID', 'CheckingAccountBalance', 'DebtsPaid', 'SavingsAccountBalance',
    #                  'CurrentOpenLoanApplications']
    # df_credit = pd.read_csv('ds-credit.tsv', sep='\s+', header=-1, names=column_credit)
    #
    # column_app = ['CustomerID', 'LoanPayoffPeriodInMonths', 'LoanReason', 'RequestedAmount', 'InterestRate',
    #               'Co-Applicant']
    # df_app = pd.read_csv('ds-app.tsv', sep='\s+', header=-1, names=column_app)
    #
    # column_borrower = ['CustomerID', 'YearsAtCurrentEmployer', 'YearsInCurrentResidence', 'Age', 'RentOrOwnHome',
    #                    'TypeOfCurrentEmployment', 'NumberOfDependantsIncludingSelf']
    # df_borrower = pd.read_csv('ds-borrower.csv', sep='\s+', index_col=False, names=column_borrower, header=0)
    #
    # column_result = ['CustomerID', 'WasTheLoanApproved']
    # df_result = pd.read_csv('ds-result.tsv', sep='\s+', header=-1, names=column_result)
    # df_result = df_result.drop_duplicates()  # Drop the duplicated results

    df = pd.read_pickle('df_corr.pkl')
    vs = Visual(df)
    # vs.compare('SavingsAccountBalance','WasTheLoanApproved')
    vs.dist('RequestedAmount', 'WasTheLoanApproved')