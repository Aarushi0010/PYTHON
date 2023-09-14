# we can iterate through the list 
# using for loop 
list = [1 , 2 , 3 , 4 , 5]
for x in list:
    print(x)

# iterate using index numbers 
# using range() and len() functions
list = [1 , 2 , 3 , 4 , 5]
for i in range(len(list)):
    print(list[i])

# using while loop 
list = [1 , 2 , 3 , 4 , 5]
while i < len(list):
    print(list[i])
    i = i + 1

# list comprehension
# shortest syntax for looping through list
list = [1 , 2 , 3 , 4 , 5]
[print(x) for x in list] 