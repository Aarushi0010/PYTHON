# we can iterate through the items in the tuple 
# 1. using for loop
my_tuple = ["apple" , "banana" , "litchi"]
for x in my_tuple:
    print(x) 

# 2. using index numbers 
for x in range(len(my_tuple)):
    print(my_tuple[x])
    
# using while loop
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i = i + 1
