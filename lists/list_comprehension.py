# list comprehension provides the shorter syntax to create a new list 
# based on an already existing list

# without list comprehension
fruits = ["apple" , "grapes" , "melon" , "cherry"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# with list comprehension

fruits = ["apple" , "grapes" , "melon" , "cherry"]
newlist = [ x for x in fruits if "a" in x]
print(newlist)

# important example
fruits = ["apple" , "banana" , "grapes" , "banana"]

newlist =[x if x!= "banana" else "fruit" ]
print(newlist)