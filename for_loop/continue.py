# It will stop the current iteration and continue with the next one 

numbers = [1 , 2 , 3 , 4 , 5 ]
for i in numbers:
    if i == 3:
        continue
    print(i)