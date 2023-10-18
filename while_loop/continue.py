# This statement stops with the current iteration and starts with the next

i = 1
while i<6:
    i = i + 1
    if i == 6:
        continue
    print(i)