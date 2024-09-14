# List Comprehension
salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x


print([new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries])

students = ["John", "Mark", "Venessa", "Mariam"]
students_not = ["John", "Venessa"]

print([student.lower() if student in students_not else student.upper() for student in students])
print([student.upper() if student not in students_not else student.lower() for student in students])

# Dict Comprehension
dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

print({k: v ** 2 for (k, v) in dictionary.items()})
print({k.upper(): v for (k, v) in dictionary.items()})

# Ex: Square even numbers and add a dict.

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2
print(new_dict)
print({n: n ** 2 for n in numbers if n % 2 == 0})

# List & Dict Comp.
# EX.: Rename Columns in a DataSet
import seaborn as sns

df = sns.load_dataset("car_crashes")  # car_crashes DataFrame from seaborn
print(df.columns)

for col in df.columns:
    print(col.upper())

A = []
for col in df.columns:
    A.append(col.upper())

df.columns = A

df.columns = [col.upper() for col in df.columns]

# EX.: Add FLAG prefix that begin with INS column name. Others NO_FLAG
print(["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns])

# EX.***: Dict.: { 'total': ['mean', 'min', 'max', 'var']
#          'speeding':['mean', 'min', 'max', 'var']...}
# Work with just numeric values
import seaborn as sns

df = sns.load_dataset("car_crashes")  # car_crashes DataFrame from seaborn
print(df.columns)

for col in df.columns:
     print(col)

# num_cols = [col for col in df. columns if df[col].dtype != "O"]
# O object(categorical variables(strings))

num_cols = df._get_numeric_data().columns
dict = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    dict[col] = agg_list

new_dict = {col: agg_list for col in num_cols}
print(new_dict)
print(df[num_cols].head())

print(df[num_cols].agg(new_dict))