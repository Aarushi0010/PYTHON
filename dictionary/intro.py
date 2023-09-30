# Dictionary stores data in key:value pairs
# Data is ordered , changeable and without duplicates

my_dict = {
    "name" :"john",
    "age" : 24,
    "year" : 1999,
    "semester" : 8,
}

print(my_dict)
print(my_dict["year"])

# Duplicate values will overwrite existing values
my_dict = {
    "name" :"john",
    "age" : 24,
    "year" : 1999,
    "semester" : 8,
    "year" : 2020,
}
print(my_dict)
print(my_dict["year"])

print(len(my_dict))
print(type(my_dict))

# dict() constructor 
dict1 = dict(name = "aarushi" , semester = "5")
print(dict1)