# import seaborn as sns
# import pandas as pd
# import numpy as np
# from matplotlib import pyplot as plt
# from pandas.core.interchange import dataframe
#
# pd.set_option('display.max_columns', None)  # Get rid of 3 dots(...). Generally not prefer in dataset has many columns.
# pd.set_option('display.width', 500)  # Table ***
# df = sns.load_dataset("titanic")
#
# # Base func.:***
# # df.head()
# # df.tail()
# # df.shape
# # df.info()
# # df.columns
# # df.index
# # df.describe().T
# # df.isnull().values.any()
# # df.isnull().sum()
#
#
# def check_df(dataframe, head=5):
#     print("################### SHAPE ######################")
#     print(dataframe.shape)
#     print("################### TYPES ######################")
#     print(dataframe.dtypes)
#     print("################### HEAD ######################")
#     print(dataframe.head(head))
#     print("################### TAIL ######################")
#     print(dataframe.tail(head))
#     print("################### NA ######################")
#     print(dataframe.isnull().sum())
#     print("################### QUANTILES ######################")
#     print(dataframe.describe([0, 0.05, 0.5, 0.95, 0.99, 1]).T)
#
#
# check_df(df)
#
# df = sns.load_dataset("tips")
# check_df(df)
# # !!! More dataset : click Ctrl+load_dataset***
# import seaborn as sns
# df = sns.load_dataset("flights")
# check_df(df)
#
# # Analysis of Categorical Variables
# df = sns.load_dataset("titanic")
# df["embarked"].value_counts()
# df["sex"].unique()
# df["class"].nunique()  # for basic data
#
# # categorical variables - cols name types str ***
# cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "bool", "object"]]
# print(cat_cols)
#
# # categorical variables appear like numeric
# num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
# print(num_but_cat)
#
# # cardinal numbers(more unique num like name surname) look like categorical
# cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
# print(cat_but_car)  # Print []
#
# cat_cols = cat_cols + num_but_cat
# # if cat_but_car have elements
# cat_cols = [col for col in cat_cols if col not in cat_but_car]
# print(df[cat_cols])  # all categorical variables as i define(unique = 10)
# print(df[cat_cols].nunique())
# print([col for col in df.columns if col not in cat_cols])  # numeric var.
#
# df['survived'].value_counts()
# 100 * df["survived"].value_counts() / len(df)
#
#
# def cat_summary(dataframe, col_name):
#     print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
#                         "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
#     print("################################################################################")
#
#
# print(df, "sex")
#
# for col in cat_cols:
#     cat_summary(df, col)  # all categorical variables in dataframe
#
#
# def cat_summary(dataframe, col_name, plot=False):
#     print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
#                         "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
#     print("################################################################################")
#
#     if plot:
#         sns.countplot(x=dataframe[col_name], data=dataframe)
#         plt.show(block=True)
#
#
# cat_summary(df, "sex", plot=True)
#
# for col in cat_cols:
#     cat_summary(df, col, plot=True)  # all categorical variables graphics and info in dataframe
#
#
# df["adult_male"].astype(int)  # True=1, False=0  convert t-f to num
#
# for col in cat_cols:
#     if df[col].dtypes == "bool":
#         df[col] = df[col].astype(int)
#         cat_summary(df, col, plot=True)
#     else:
#         cat_summary(df, col, plot=True)
#
#
# # Analysis of Numerical Variables
# import seaborn as sns
# import pandas as pd
# import numpy as np
# from matplotlib import pyplot as plt
#
# pd.set_option('display.max_columns', None)  # Get rid of 3 dots(...). Generally not prefer in dataset has many columns.
# pd.set_option('display.width', 500)  # Table ***
# df = sns.load_dataset("titanic")
#
# print(df[["age", "fare"]].describe().T)
#
# print([col for col in df.columns if df[col].dtypes in ["int64", "float64"]])  # get numerical var.
#
# num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]
# num_cols = [col for col in df.columns if col not in cat_cols]
#
#
# def num_summary(dataframe, numerical_col):
#     quantiles = [0, 0.05, 0.5, 0.7,  0.95, 0.99, 1]
#     print(dataframe[numerical_col].describe(quantiles).T)
#
#
# num_summary(df, "age")
#
# for col in num_cols:       # all categorical variables info in dataframe
#     num_summary(df, col)
#
#
# def num_summary(dataframe, numerical_col, plot=False):
#     quantiles = [0, 0.05, 0.5, 0.7, 0.95, 0.99, 1]
#     print(dataframe[numerical_col].describe(quantiles).T)
#
#     if plot:  # if plot equals to true continue next step
#         dataframe[numerical_col].hist()
#         plt.xlabel(numerical_col)
#         plt.title(numerical_col)
#         plt.show(block=True)
#
#
# num_summary(df, "age", plot=True)  # age histogram graph
#
# for col in num_cols:
#     num_summary(df, col, plot=True)   # all numerical variables histogram graphics
#
#
# # Grabbing Variables and Generalizing Ops
# import seaborn as sns
# import pandas as pd
# import numpy as np
# from matplotlib import pyplot as plt
#
# pd.set_option('display.max_columns', None)  # Get rid of 3 dots(...). Generally not prefer in dataset has many columns.
# pd.set_option('display.width', 500)  # Table ***
# df = sns.load_dataset("titanic")
#
#
# def grab_col_names(dataframe, cat_th=10, car_th=20):  # Unique variable num <10 categorical, >20 cardinal variable
#     # docstring: Settings-> Docstring-> Change numPy-> 3 " + enter
#     """
#
#     Parameters
#     ----------
#     dataframe: dataframe
#         dataframe that could be take variables from
#     cat_th: int, float
#         class threshold for numerical but categorical variables
#     car_th: int, float
#         class threshold for categorical but numerical variables
#
#     Returns
#     -------
#     cat_cols: list
#         Categorical variable list
#     num_cols: list
#         Numerical variable list
#     cat_but_car: list
#         Cardinal variables list looks like categorical
#
#     Notes
#     ------
#     cat_cols + num_cols + cat_but_car = total variable number
#     num_but_cat in cat_cols
#
#     """
#
#     cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "bool", "object"]]
#     num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
#     cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
#
#     cat_cols = cat_cols + num_but_cat
#     cat_cols = [col for col in cat_cols if col not in cat_but_car]
#
#     num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]
#     num_cols = [col for col in df.columns if col not in cat_cols]
#
#     print(f"Observations: {dataframe.shape[0]}")
#     print(f"Variables: {dataframe.shape[1]}")
#     print(f'cat_cols: {len(cat_cols)}')
#     print(f'num_cols: {len(num_cols)}')
#     print(f'cat_but_car: {len(cat_but_car)}')
#     print(f'num_but_cat: {len(num_but_cat)}')
#
#     return cat_cols, num_cols, cat_but_car
#
#
# cat_cols, num_cols, cat_but_car = grab_col_names(df)
#
# cat_summary(df, "sex")
# for col in cat_cols:
#     cat_summary(df, col)
#
# for col in num_cols:
#     num_summary(df, col, plot=True)
#
# # bonus: convert Bool type variables to Integer with astype function and use cat_summary func.(visual) effectively
# df = sns.load_dataset("titanic")
# df.info()
# for col in df.columns:
#     if df[col].dtypes == "bool":
#         df[col] = df[col].astype(int)
#
# cat_cols, num_cols, cat_but_car = grab_col_names(df)
#
# for col in cat_cols:
#     cat_summary(df, col, plot=True)
#
# for col in num_cols:
#     num_summary(df, col, plot=True)
#
#
# # Analysis of Target Variable
#
# # survived variable is target.
#
# # Analysis Target Variable with categorical variables
# print(df.groupby("sex")["survived"].mean())  # Being a female(%74) affect survived variable
#
#
# def target_summary_with_cat(dataframe, target, categorical_col):
#     print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")
#
#
# target_summary_with_cat(df, "survived", "pclass")  # First class passengers(%62) survived more
#
# for col in cat_cols:
#     target_summary_with_cat(df, "survived", col)
#
# # Analysis Target Variable with numerical variables
# print(df.groupby("survived")["age"].mean())  # Change axis. Age Means of survived(1)= 28yo, death(0)= 30yo
# print(df.groupby("survived").agg({"age": "mean"}))  # Same output with above but more readable
#
#
# def target_summary_with_num(dataframe, target, numerical_col):
#     print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")
#
#
# target_summary_with_num(df, "survived", "age")
#
# for col in num_cols:
#     target_summary_with_num(df, "survived", col)
#
#
# Analysis of Correlation ***
# Correlation is the statistical measure that defines to which extent two variables are linearly related to each other.
# Denoted by r, it takes values between -1 and +1.Correlation summarizes the strength and
# direction of the linear (straight-line) association between two quantitative variables.

import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)  # Get rid of 3 dots(...). Generally not prefer in dataset has many columns.
pd.set_option('display.width', 500)  # Table ***
df = pd.read_csv("breast_cancer.csv")
df = df.iloc[:, 1:-1]
print(df.head())

num_cols = [col for col in df.columns if df[col].dtypes in [int, float]]
corr = df[num_cols].corr()  # correlation function
print(corr)

# heat map
sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

# deleting high correlation variables
cor_matrix = df[num_cols].corr().abs()  # doesn't matter positive or negative value so use absolute value function

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_))
print(upper_triangle_matrix)

drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]
print(drop_list)
print(cor_matrix[drop_list])
df.drop(drop_list, axis=1)  # delete drop list(10 variables)
print(df.shape)


def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    numerical_col = [col for col in dataframe.columns if dataframe[col].dtype in [int, float]]
    corr = dataframe[numerical_col].corr()
    cor_matrix = df[num_cols].corr().abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list


high_correlated_cols(df)
drop_list = high_correlated_cols(df, plot=True)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1), plot=True)  # get rid of high correlated values(1.0_navy,-1.0_burgundy)


