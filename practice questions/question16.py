string1 = input("Enter the string : ")
p = ""
for char in string1:
    if char not in p:
        p = p + char
print (p)
