dict1 = {
    "name" : "aarushi",
    "year" : 2021,
    "semester" : 5,
    "language" : "python"
}

# 1. get() method
x = dict1.get("language")
print(x)

# 2. keys() method  [list of all keys in the dictionary]
y = dict1.keys()
print(y)

# 3. values() method  [list of all values in the dictionary]
z = dict1.values()
print(z)

# 4. items() method  [displays the dictionary items as tuples in a list]
a = dict1.items()
print(a)

# if condition  [only for keys]
if "name" in dict1:
    print("correct option")