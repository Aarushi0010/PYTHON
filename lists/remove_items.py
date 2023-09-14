# using remove() method
list = [1 , 2 , 3 , 4 , 5]
list.remove(3)
print(list)

# using pop() method 
# removing element from specific index
list = [1 , 2 , 3 , 4 , 5]
list.pop(4)
print(list)

# if no index specified , them last item removed
list = [1 , 2 , 3 , 4 , 5]
list.pop()
print(list)

# del removes item at specified index
list = [1 , 2 , 3 , 4 , 5]
del list[2]
print(list)

# del can also be used to delete the entire list
list = [1 , 2 , 3 , 4 , 5]
del list

# clear() method used to empty the list 
list = [1 , 2 , 3 , 4 , 5]
list.clear()
print(list)