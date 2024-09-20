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
import seaborn as sns
df = sns.load_dataset("flights")
check_df(df)

# Analysis of Categorical Variables
df = sns.load_dataset("titanic")
df["embarked"].value_counts()
df["sex"].unique()
df["class"].nunique()  # for basic data

# categorical variables - cols name types str ***
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "bool", "object"]]
print(cat_cols)

# categorical variables appear like numeric
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
print(num_but_cat)

# cardinal numbers(more unique num like name surname) look like categorical
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
print(cat_but_car)  # Print []

cat_cols = cat_cols + num_but_cat
# if cat_but_car have elements
cat_cols = [col for col in cat_cols if col not in cat_but_car]
print(df[cat_cols])  # all categorical variables as i define(unique = 10)
print(df[cat_cols].nunique())
print([col for col in df.columns if col not in cat_cols])  # numeric var.

df['survived'].value_counts()
100 * df["survived"].value_counts() / len(df)


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))


print(df, "sex")

for col in cat_cols:
    cat_summary(df, col)  # all categorical variables in dataframe

