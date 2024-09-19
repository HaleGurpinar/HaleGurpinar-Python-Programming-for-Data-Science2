# MATPLOTLIB  &  SEABORN
# Categorical variable --> M: bar chart,  S: countplot
# Numerical variable --> Histogram and boxplot

# Categorical Variable Visualization
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind="bar")  # !!! pip install matplotlib  or  pip install --upgrade matplotlib
plt.show()


# Numerical Variable Visualization
plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()

# MATPLOTLIB
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# plot
x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])
plt.plot(x, y)
plt.show()

# marker : markers['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']
x = np.array([13, 28, 11, 100])
plt.plot(x, marker='o')
plt.show()
x = np.array([13, 28, 11, 100])
plt.plot(x, marker='*')
plt.show()

# line
y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashed")
plt.show()
y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dotted")
plt.show()
y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashdot", color="r")
plt.show()

# multiple lines
x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])
plt.plot(x)
plt.plot(y)
plt.show()

# labels
x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])
plt.plot(x, y)
plt.title("Main Header")
plt.xlabel("X axis:  Name")
plt.ylabel("Y axis: Name")
plt.grid()  # to increase readability
plt.show()

# subplots
# plot 1
x = np.array([20, 45, 60, 85, 105])
y = np.array([10, 30, 55, 70, 95])
plt.subplot(1, 2, 1)  # create 1st plot  1 row 2 column graph
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([25, 55, 65, 95, 115])
y = np.array([250, 230, 210, 205, 200])
plt.subplot(1, 2, 2)  # create 2nd plot  1 row 2 column graph
plt.title("2")
plt.plot(x, y)
plt.show()

# SEABORN
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = sns.load_dataset("tips")

df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)  # Categorical Vis.
plt.show()

sns.boxplot(df["total_bill"])  # Numerical Vis.
plt.show()

df["total_bill"].hist()  # Numerical Vis.
plt.show()