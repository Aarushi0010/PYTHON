# 1. using index 
tuple = ("apple" , "banana" , "mango")
print(tuple[1])

# 2. using negative index
tuple = ("apple" , "banana" , "mango")
print(tuple[-1])

# 3. using range of indexes
tuple = ("apple" , "banana" , "mango" , "orange" , "guava" , "litchi")
print(tuple[2:4])

print(tuple[:4])

print(tuple[2:])

print(tuple[-5:-2])

# to check if item is present in the tuple
if "grapes" in tuple:
    print("item found")
else:
    print("Invalid item")