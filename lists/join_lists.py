# methods used for joining or concatenating two or more lists
# 1. using + operator

list1 = [1 , 2 , 3 , 4 , 5]
list2 = [6 , 7 , 8 , 9 , 10]
list3 = list1 + list2
print(list3) 

# 2. append() method
list1 = [1 , 2 , 3 , 4 , 5]
list2 = [6 , 7 , 8 , 9 , 10]
for x in list2:
    list1.append(x)
print(list1)
print(list2)

# 3. using extend() method 
list1 = [1 , 2 , 3 , 4 , 5]
list2 = [6 , 7 , 8 , 9 , 10]
list1.extend(list2)
print(list1)
print(list2) 