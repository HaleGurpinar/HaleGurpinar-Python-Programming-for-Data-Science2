# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.
# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis".

# Pandas Series: A Pandas Series is like a column in a table, It is a one-dimensional array holding data of any type.
import pandas as pd

print(pd.Series([25, 10, 12, 4, 5]))
s = pd.Series([25, 10, 12, 4, 5])
print(type(s))
print(s.index)
print("PSeries dtype: ", s.dtype, "Size: ", s.size, "Dimension:", s.ndim)
print(s.values)  # Return NumPy Array
print(s.head(3))
print(s.tail(3))

# Pandas DataFrames: Data sets in Pandas are usually multidimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.

# Reading Data
import pandas as pd

df = pd.read_csv("Dataset/advertising.csv")  # To read another type file: Ctrl+pd click,Ctrl+F search with "read" key.
print(df.head())

# Pandas CheatSheet ***

# Quick Look at Data
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
print("Head", df.head(), "Tail", df.tail())
print("Dimension Info.:", df.shape)
print("Info.", df.info)
print("Index: ", df.index)
print("Columns", df.columns)
print(df.describe().T)  # Return statistics (T means transpose.It used for clear output)

print(df.isnull().values.any())  # Is there any(at least one) null value in dataframe? ******
# Are there any missing values in the data frame?

print(df.isnull().sum())  # Return that each variable's missing values count

print(df["sex"].value_counts())
print(df["alive"].value_counts())

# Selection in Pandas****
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.index)
print(df[0:13])

df.drop(0, axis=0).head()  # Delete 0. index, axis=0(rows) -> Delete 1st row
delete_index = [1, 2, 3, 7]
df.drop(delete_index, axis=0).head(10)  # Delete arrays index rows from dataframe.This is not a permanent way to delete.

# df = df.drop(delete_index, axis=0)          # Permanent Delete
# df.drop(delete_index, axis=0, inplace=True) # Permanent Delete

# Convert Variable to Index***
df["age"].head()
df.age.head()

print(df.index)
df.index = df["age"]
print(df.index)
print(df.drop("age", axis=1).head())  # Delete "age" index so axis=1(columns). Temporary Delete
print(df.drop("age", axis=1, inplace=True))  # Permanent Delete from Dataframe

# 1.) Convert Index to Variable***
# df["age"]  # KeyError(key) because deleted before "age
print(df)
df["age"] = df.index  # Create "age" named variable and assign indexes values.
print(df.head())

# 2.) Convert Index to Variable***
print(df.drop("age", axis=1, inplace=True))
print(df.reset_index().head())  # Delete value in index and add as a new variable(as a column)
df = df.reset_index()
print(df.head())

# Operations with Variables(Columns)
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)  # Get rid of 3 dots(...). Generally not prefer in dataset has many columns.
df = sns.load_dataset("titanic")

print("age" in df)  # Dataframe include "age" variable?
print(type(df["age"].head()))  # pandas.core.series.Series

# ***!!! [[]] keeps your data as a DataFrame***
print(type(df[["age"]].head()))  # pandas.core.frame.DataFrame

print(df[["age", "alive"]])
col_names = ["age", "alive"]
print(df[col_names])  # same output with [[]]

df["age2"] = df["age"] ** 2  # Add as a new name and new values
print(df.head())
df["age3"] = df["age"] / df["age2"]
print(df)

print(df.drop("age3", axis=1).head())  # Delete age3 column
print(df.drop(col_names, axis=1).head())  # Delete col_names values variables

print(df.loc[:, df.columns.str.contains("age")].head())  # Columns names have "age" str, loc used selection from df
print(df.loc[:, ~df.columns.str.contains("age")].head())  # # Columns names have not "age" str


# iloc(integer based selection) & loc(label based selection)***
print(df.iloc[0:3])  # 0,1,2
print(df.loc[0:3])  # 0,1,2,3

col_names = ["age", "embarked", "alive"]
print(df.loc[0:3, col_names])  # 0,1,2,3 rows "age", "embarked", "alive" columns contain str+float**


# Conditional Selection
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)  # Get rid of 3 dots(...). Generally not prefer in dataset has many columns.
df = sns.load_dataset("titanic")
print(df.head())

print(df[df["age"] > 50].head())  # Age > 50 people from dataset
print(df[df["age"] > 50]["age"].count())  # count Age > 50 people from dataset

print(df.loc[df["age"] > 50, "class"].head())
print(df.loc[df["age"] > 50, ["age", "class"]].head())

# !!!! If there ara more than 1 condition, parenthesis all conditions statements***
print(df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head())

print(df.loc[(df["age"] > 50)
             & (df["sex"] == "male")
             & (df["embark_town"] == "Cherbourg"), ["age", "class", "embark_town"]].head())  # 3 conditions

print(df.loc[(df["age"] > 50)
             & (df["sex"] == "male")
             & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
            ["age", "class", "embark_town"]].head())  # 3 conditions

print(df["embark_town"].value_counts())


# Aggregation & Grouping
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)  # Get rid of 3 dots(...). Generally not prefer in dataset has many columns.
df = sns.load_dataset("titanic")

print(df.groupby("sex")["age"].mean())  # Mean age by sex
print(df.groupby("sex").agg({"age": "mean"}))
print(df.groupby("sex").agg({"age": ["mean", "sum", "max"]}))
print(df.groupby("sex").agg({"age": ["mean", "sum"], "survived": "mean"}))
print(df.groupby(["sex", "embark_town"]).agg({"age": ["mean"], "survived": "mean"}))  # 2 level grouping
print(df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"], "survived": "mean"}))
print(df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"}))

# Pivot Table
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)  # Get rid of 3 dots(...). Generally not prefer in dataset has many columns.
pd.set_option('display.width', 500)                  # Table ***
df = sns.load_dataset("titanic")

print(df.pivot_table("survived", "sex", "embarked"))  # pivot_table(values, row-index, column)***default value ops: mean
print(df.pivot_table("survived", "sex", "embarked", aggfunc="std"))  # Standard Deviation
print(df.pivot_table("survived", "sex", ["embarked", "class"]))  # 2 level

# !!! cut and qcut functions are commonly used for converting numerical variables to categorical***
# If you know(age: 0-3 baby, 3-4 toddler, 18 adult) which categories you want to divide numeric values into,
# use the cut function. Don't kow use qcut function.***
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
print(df.head())

print(df.pivot_table("survived", "sex", "new_age"))
print(df.pivot_table("survived", "sex", ["new_age", "class"]))

