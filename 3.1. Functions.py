def calculate(x):
    print(x * 2)


calculate(5)


def sum_f(arg1, arg2):
    print(arg1 + arg2)


sum_f(15, 30)


#  Docstring
def summer(arg1, arg2):
    """
    Sum of two numbers

    :param arg1: int, float
    :param arg2: int, float
    :return:
    """
    print(arg1 + arg2)


summer(10, 8.5)


# Function Statement
def mult(a, b):
    c = a * b
    print(c)


mult(10, 9)

list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(21, 4)
add_element(20, 5)

def divide(a, b = 1):
    print(a / b)


divide(1)

def calculate(warm, moisture, charge):
    print((warm + moisture) / charge)


def calculate(warm, moisture, charge):
    return (warm + moisture) / charge


print(calculate(98, 12, 78) * 10)

def calculate(warm, moisture, charge):
    warm = warm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (warm + moisture) / charge
    return warm, moisture, charge, output


print(calculate(98, 12, 78))

warm, moisture, charge, output = calculate(98, 12, 78)

def all_calc(warm, moisture, charge, p):
    a = calculate(warm, moisture, charge)
    b = summer(a, p)
    print(b * 10)


print(all_calc(1, 3, 5, 10))