# using keyword to customize your function
def myfun(n):
    return abs(n-50)

list = [100 , 300 , 50 , 40 , 200]
list.sort(key = myfun)

print(list)

# sort() is case sensitive so capital letters are sorted before lower case letters
list = ["aarushi" , "Japleen" , "vivek" , "Ujwal"]
list.sort()
print(list)

# to have case insensitive sorting we use str.lower as keyword
list = ["aarushi" , "Japleen" , "vivek" , "Ujwal"]
list.sort(key = str.lower)
print(list)

# reverse() method reverses the entire list 
list = ["aarushi" , "Japleen" , "vivek" , "Ujwal"]
list.reverse()
print(list)