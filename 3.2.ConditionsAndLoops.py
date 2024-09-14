# if
if 1 == 1:
    print("that's true")


def num_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")


num_check(12)


def num_check(number):
    if number > 10:
        print("number is greater than 10")
    elif number < 10:
        print("number is less than 10")
    else:
        print("number is equal to 10")


num_check(23)

# for
students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

salaries = [1000, 2000, 3000, 4000]
for salary in salaries:
    print(int(salary * 20 / 100 + salary))


def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)


print(new_salary(1500, 10))
for salary in salaries:
    print(new_salary(salary, 10))

for salary in salaries:
    if salary >= 3000:
        print("If salary is equal to 3000 or greater than 3000", new_salary(salary, 10))
    else:
        print("If salary is less than 3000", new_salary(salary, 20))


# #########################################################################################################################################################

# Ex.:  "Alternating"
# Input: "hi my name is john and i am learning python"
# Output: "Hi mY NaMe iS JoHn aNd i aM LearNiNg pYtHoN"
# Tip: Even index is capital letter and odd index is lower case letter.
def alternating(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    print(new_string)


alternating("hi my name is john and i am learning python")
# ############################################################################################################################################################

# BREAK:Skip others if break cond. is true, CONTINUE:Skip just cond. value  if cond. is true,
# WHILE: Continue to work until cond. is true
salaries = [100, 200, 300, 400]
for salary in salaries:
    if salary == 300:
        break
    print(salary)

for salary in salaries:
    if salary == 300:
        continue
    print(salary)

number = 1
while number < 5:
    print(number)
    number += 1

# Enumerate
students = ["John", "Mark", "Venessa", "Mariam"]
for i, student in enumerate(students, 1):
    print(i, student)

A = []
B = []
for i, student in enumerate(students):
    if i % 2 == 0:
        A.append(student)
    else:
        B.append(student)

print(A, B)

# ######################################################################################################################################################
# Ex.: Define a divide_students function.
# 1st List students who placed in even index and 2nd List students who placed in even index.
# Return a list that combined 2 list.

students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(students):
    groups = [[], []]
    for i, student in enumerate(students):
        if i % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups


divide_students(students)


# ############################################################################################################################################################
# Ex.: Alternating Func. with Enumerate


def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)


alternating_with_enumerate("hi my name is john and i am learning python")

# Zip
students = ["John", "Mark", "Venessa"]
departments = ["engineering", "statistics", "astronomy"]
ages = [21, 19, 20]

print(list(zip(students, departments, ages)))

# Lambda, Map, Filter, Reduce
x = lambda a, b: a + b
print(x(4, 5))

salaries = [100, 200, 300, 400, 500]


def new_salary(x):
    return x * 20 / 100 + x


for salary in salaries:
    print(new_salary(salary))

print(list(map(new_salary, salaries)))
print(list(map(lambda x: x * 20 / 100 + x, salaries)))

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, list_store)))

from functools import reduce

list_store = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, list_store))