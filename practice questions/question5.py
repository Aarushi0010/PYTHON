list=[]
index=[]
n=int(input("Enter Number of Elements in List = "))
for i in range (n):
    num=int(input("Enter element ="))
    list.append(num)
element=int(input("Enter Elements to find in list = "))
for j,item in enumerate(list):
    if item == element:
        index.append(j)
if index==[]:
    print("The target value ",element," is not in the list.")
else:
    print("The target value ",element,"  is found at positions:",index)
