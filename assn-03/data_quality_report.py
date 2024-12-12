import pandas as pd
import math
from tabulate import tabulate


def missing(df):
    x = df.isna().sum()
    y = []
    for row in x:
        y.append(row)

    return y


def cardinality(df):
    x = df.nunique()
    y = []
    for row in x:
        y.append(row)
    return y


def mode(df, i):
    x = df.mode().loc[i]
    y = []
    for row in x:
        y.append(row)
    return y


def mode_frequency(df, mod):
    i = 0
    y = []
    for column in df:
        x = df[column].value_counts()
        if pd.isna(mod[i]):
            y.append(float('nan'))
        else:
            y.append(x[mod[i]])
        i = i+1
    return y


def mode_percent(count, mod_freq):
    x = []
    for y in mod_freq:
        x.append((y/count) * 100)
    return x


# print data quality report for categorical features
def categorical(df):
    # get the categorical features from the dataframe
    columns = df.loc[:, ['Week', 'HomeTeam', 'AwayTeam', 'Result']]
    # count for our features
    count = len(columns)
    # get missing values for our features
    missing_values = missing(columns)
    # get cardinality for features
    card = cardinality(columns)
    # get 1st mode
    mod = mode(columns, 0)
    # get 1st mode frequency
    mod_freq = mode_frequency(columns, mod)
    # get 1st mode percentage
    mod_per = mode_percent(count, mod_freq)
    # get 2nd mode
    mod2 = mode(columns, 1)
    # get 2nd mode frequency
    mod2_freq = mode_frequency(columns, mod2)
    # get 2nd mode percentage
    mod2_per = mode_percent(count, mod2_freq)
    my_data = []
    i = 0
    for row in columns:
        y = [row, count, missing_values[i], card[i], mod[i], mod_freq[i], mod_per[i], mod2[i], mod2_freq[i], mod2_per[i]]
        my_data.append(y)
        i = i+1
    # column labels for our table
    head = ["feature", "count", "% Miss.", "Card.", "Mode", "Mode Freq.", "Mode %", "2nd Mode", "2nd Mode Freq.", "2nd Mode %"]
    print(tabulate(my_data, headers=head, tablefmt="grid"))


def main():
    x = pd.read_csv("game_stats_2018.csv")
    y = pd.read_csv("game_stats_2019.csv")
    df_2018 = pd.DataFrame(x)
    df_2019 = pd.DataFrame(y)
    print("DQR: Categorical Features 2018")
    categorical(df_2018)
    print("DQR: Categorical Features 2019")
    categorical(df_2019)
