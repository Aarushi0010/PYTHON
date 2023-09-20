# Tuples are used to store multiple items in a single variable
# key difference between list and tuple is that tuples are immutable while lists 
# are mutable(i.e the data items can be changed in a list and not in a tuple)

# example 
tuple = (1 , 2 , 3)
print(tuple)

# find length of tuple using len() function
tuple = (1 , 2 , 3)
print(len(tuple))

# create a tuple with only one item using ,
tuple = ("hello" ,)
print(tuple)

# can be of any data types
tuple = ("aarushi" , 22 , True)
print(tuple)
print(type(tuple))

# create a tuple using tuple() constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)