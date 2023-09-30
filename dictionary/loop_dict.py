dict1 = {
    "name" : "aarushi",
    "year" : 2021,
    "semester" : 5,
    "language" : "python",
    "ID" : 22,
    "section" : "A1"
}

#1. for loop
for x in dict1:
    print(x)

# 2. values() method  [to print only the values of the dictionary]
for x in dict1.values():
    print(x)

# 3. keys() method  [to print only the keys of the dictionary]
for x in dict1.keys():
    print(x)

# 4. items() method  [to print both the keys and the values]
for x,y in dict1.items():
    print(x, ":" ,y)