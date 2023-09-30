# 1. referring its key name 
dict1 = {
    "name" : "aarushi",
    "year" : 2021,
    "semester" : 5,
    "language" : "python"
}

dict1["year"] = 2020
print(dict1["year"])

# 2. update() method 

dict1.update({"name" : "Japleen"})
print(dict1["name"])