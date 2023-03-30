import pandas as pd

filepath = '../data/interim/sales.csv'

def get_df():
    df = pd.read_csv(filepath)
    df.set_index(df.Months, drop = True, inplace = True)
    df.drop('Months', axis = 1, inplace = True)
    return df