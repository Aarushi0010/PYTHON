# As tuples are unchangeable or immutable , we convert the tuple into a list 
# and then change the item , followed by converting of list back into tuple

x = ("apple" , "banana" , "litchi")
y = list(x)
y[0] = "orange"
x = tuple(y)
print(x)
print(type(x))

# 1. Add item
x = ("apple" , "banana" , "litchi")
y = list(x)
y.append("guava")
x = list(y)
print(x)

# 2. Add tuple to a tuple 
x = ("apple" , "banana" , "litchi")
y = ("guava" , "orange")
x = x + y
print(x)

# 3. Remove item from tuple
x = ("apple" , "banana" , "litchi")
y = list(x)
y.remove("litchi")
x = tuple(y)
print(x)

# 4. Delete the tuple
x = ("apple" , "banana" , "litchi")
del x
print(x)
