# It breaks the for loop even if all the items are not looped 

numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
for i in numbers:
    
    if i >=6:
        break
    print(i)