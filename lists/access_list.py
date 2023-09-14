# using index 
list = ["apple" , "banana" , "cherry"]
print(list[0])

# negative indexing
print(list[-2])

# range of indexes 
# end index is excluded 
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[2:5])

# range of negative indexes
print(list[-4:-1])

# if item present in the list
if "apple" in list:
    print("yes! , item found")