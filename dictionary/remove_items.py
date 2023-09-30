# 1. pop() method  [with specified key names]
dict1 = {
    "name" : "aarushi",
    "year" : 2021,
    "semester" : 5,
    "language" : "python",
    "ID" : 22,
    "section" : "A1"
}
dict1.pop("language")
print(dict1["language"])

# 2. del() method  [deletes the entire dictionary]
del dict1
print(dict1)

# 3. clear() method  [empties the entire dictionary]
dict1.clear()

# 4. popitem() method  [pops the last added element to the dictionary]
dict1.popitem()
