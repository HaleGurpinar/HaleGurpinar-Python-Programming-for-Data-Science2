# NumPy: Numerical Python
# Why Numpy?: 1. Faster than list because store the data efficiently and fixed type array.
# 2. High level(functional, vector) calculations like multiply 2 matrix, array.
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
print(a * b)

# Create NumPy Array
import numpy as np
np.array([1, 2, 3, 4, 5])
print(type(np.array([1, 2, 3, 4, 5])))
print(np.zeros(10, dtype=int))
print(np.random.randint(0, 10, size=10))
print(np.random.normal(10, 4, (3, 4)))  # normal(mean, standard deviation, size= 3x4)

# Attributes of NumPy Array

# ndim: Number of dimension
# shape: Dimension info.
# size : Number of total elements
# dtype : Type of array data
import numpy as np
a = np.random.randint(10, size=5)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

# Reshaping
import numpy as np
a = np.random.randint(1, 10, size=9)
print(a)
print(a.reshape(3, 3))
print(np.random.randint(1, 10, size=9).reshape(3, 3))

# Index Selection
import numpy as np
m = np.random.randint(10, size=(3, 5))
print(m)
print(m[0, 0])
print(m[1, 1])

m[2, 3] = 999
print(m)

m[2, 3] = 2.159
print(m)   # Store just one type value so addition value should be same as others

print(m[:, 0])  # All rows and 0. column
print(m[1, :])  # 1st row and all columns
print(m[0:2, 0:3])

arr = np.array([100, 200, 300, 400, 500])
print("Negative index of Array Examples")
print(arr[-3:-1])   # Negative numbers mean that you count from the right instead of the left.
# So, list[-1] refers to the last element, list[-2] is the second-last, and so on.

# Fancy Index
import numpy as np
v = np.arange(0, 30, 3)  # From 0 to 30 three by three
print(v)
catch = [0, 1, 2, 5]
print(v[catch])

# Conditions on NumPy
import numpy as np
v = np.array([1, 2, 3, 34, 555, 6, 7, 8])
print(v < 3)
print(v[v < 5])
print(v[v != 3])
print(v[v >= 6])

# Mathematical Operations
import numpy as np
v = np.array([10, 20, 30, 40, 50, 60])
print(v / 5)
print(v * 5 / 10)
print(v ** 2)
print(v - 5)

print(np.add(v, 1))
print(np.subtract(v, 5))
print(np.mean(v))
print(np.sum(v))
print(np.min(v))
print(np.max(v))
print(np.var(v))  # Variance of array

# Equation with two unknowns solution with NumPy
# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])  # Coefficients
b = np.array([12, 10])
print(np.linalg.solve(a, b))