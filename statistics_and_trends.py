"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.scatter(df['GDP per capita'], df['Healthy life expectancy'], marker='o', s=50, c=df['Score'], cmap='RdYlGn', edgecolor='black')
    plt.colorbar(label='Score')
    plt.xlabel('GDP per capita')
    plt.ylabel('Healthy life expectancy')
    plt.title('GDP per capita vs Healthy life expectancy')
    plt.show()
    plt.savefig('relational_plot.png')
    return


def plot_categorical_plot(df):
    fig, ax = plt.subplots(figsize=(6, 30))
    ax.barh(df['Country or region'], df['Score'], color='green')  
    ax.set_xlabel('Score')
    ax.set_ylabel('Country or Region')
    ax.set_title('Categorical Plot of Countries and Scores')
    plt.tight_layout()
    plt.savefig('categorical_plot.png')
    plt.show()
    return



def plot_statistical_plot(df):
    fig, ax = plt.subplots(dpi=144)
    corr_matrix = df.corr()
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(corr_matrix, ax=ax, vmin=-1, vmax=1, cmap='RdBu', annot=True, mask=mask, linewidths=0.5, fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.savefig('statistical_plot.png')
    return


def statistical_analysis(df, col: str):
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col])
    excess_kurtosis = ss.kurtosis(df[col])
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    df.describe()
    df.head()
    df.tail()
    df.corr
    return df


def writing(moments, col):
    mean, stddev, skew, excess_kurtosis = moments
   
    skew_desc = "not skewed"
    if skew > 0.5:
        skew_desc = "right-skewed"
    elif skew < -0.5:
        skew_desc = "left-skewed"

    kurt_desc = "mesokurtic"
    if excess_kurtosis > 1:
        kurt_desc = "leptokurtic"
    elif excess_kurtosis < -1:
        kurt_desc = "platykurtic"
    
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    print(f'The data is {skew_desc} and {kurt_desc}.')
    return

def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = 'Score'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return 
if __name__ == '__main__':
    main()
