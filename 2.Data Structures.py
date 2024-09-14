# Numbers: int, float, complex
a = 5
b = 10.1
c = 3j + 7

print(type(a), type(b), type(c))
print(int(a * b) + 4)

# Strings: "Hello World!"
print("I'm billionaire.")

str = """Data Structure: ,
Numbers: int,float,complex,
Characters Arrays(Strings),
List,Dictionary, Tuple, Set,
Boolean (TRUE-FALSE): bool"""
print(str)
print(str[2])
print(str[0:35])
print("ool" in str)
print("list" in str)

# String Methods
print(dir(int))
print(dir(str))

name = "Tom Alter"
print(len(name))
print(name.upper())
print(name.lower())
print(name.replace("o", "i"))

print(" offfofo ".strip())
print("offfofo".strip("o"))

print("cool".capitalize())
dir("cool")
print("cool".startswith("c"))

# List: List items are ordered, changeable, and allow duplicate values.
notes = [1, 2, 3, 4]
type(notes)

names = ["ab", "cde", "def", "hg"]
not_nam = [5, 8, "h", "g", True, [1, 2, 3]]
print(not_nam[3])
print(not_nam[5][0])
not_nam[0] = 100
print(not_nam)
print(not_nam[0:5])

dir(notes)
len(notes)
notes.append(500)
print(notes)
notes.pop(4)
print(notes)
notes.insert(4, 5)
print(notes)

# Dictionaries: Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*(after 3.7; 3.6 and earlier dictionaries  are unordered),
# changeable and do not allow duplicates.

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg",
              "NUM": ["COM", 10, 20, 30]
              }

print(dictionary["LOG"])
print(dictionary["NUM"])
print(dictionary["NUM"][2])

print("Regression" in dictionary)  # Search in keys
print("CART" in dictionary)
print(dictionary.get("LOG"))
dictionary["REG"] = ["YSA", 10]
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
dictionary.update({"REG": 11})  # use for add new key-value and update
dictionary.update({"RF": 80})
print(dictionary)

# Tuple: used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable.
t = ("tom", "tim", 1, 2)
type(t)
print(t[0])
print(t[0:3])

# Set:  store multiple items in a single variable.(UNIQUE)
# A set is a collection which is unordered, unchangeable(can remove items and addd new items), and unindexed.

set1 = {1, 3, 5}
set2 = {1, 2, 3}
type(set1)
set1.difference(set2)  # Items from the first set that are not in the other set(s).
print(set1 - set2)

set1.symmetric_difference(set2)  # all items EXCEPT the duplicates(only the elements that are NOT present in both sets)
print(set1 ^ set2)

set1.intersection(set2)  # ONLY the duplicates(only contains the items that are present in both sets.)
print(set1 & set2)

set1.union(set2)  # union() and update() methods joins all items from both sets.
print(set1 | set2)

set1.isdisjoint(set2)  # Returns true two sets  intersection empty
set1.issubset(set2)  # Return true first set is other's subset
set1.issuperset(set2)  # Return true first set contain other