import seaborn as sns
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)  # Get rid of 3 dots(...). Generally not prefer in dataset has many columns.
pd.set_option('display.width', 500)  # Table ***
df = sns.load_dataset("titanic")

# Base func.:***
# df.head()
# df.tail()
# df.shape
# df.info()
# df.columns
# df.index
# df.describe().T
# df.isnull().values.any()
# df.isnull().sum()


def check_df(dataframe, head=5):
    print("################### SHAPE ######################")
    print(dataframe.shape)
    print("################### TYPES ######################")
    print(dataframe.dtypes)
    print("################### HEAD ######################")
    print(dataframe.head(head))
    print("################### TAIL ######################")
    print(dataframe.tail(head))
    print("################### NA ######################")
    print(dataframe.isnull().sum())
    print("################### QUANTILES ######################")
    print(dataframe.describe([0, 0.05, 0.5, 0.95, 0.99, 1]).T)


check_df(df)

df = sns.load_dataset("tips")
check_df(df)
# !!! More dataset : click Ctrl+load_dataset***
df = sns.load_dataset("flights")
check_df(df)