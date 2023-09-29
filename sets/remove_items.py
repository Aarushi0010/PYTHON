# 1. using remove() method [It raises an error if item is not present]
set1 = {1 , 2 , 3 , 4 , 5}
set1.remove(4)
print(set1)

# 2. using discard() method [It raises no error if item is not present]
set1.discard(2)
print(set1)

# 3. using pop method  [it randomly removes an item]
set2 = {6 , 7 , 8 , 9 , 10}
x = set2.pop
print(x)
print(set2)

#4. using clear() method [empties the entire set]
set1.clear()
print(set1)

# 5. using del() method [deletes the entire set]
del set2
print(set2)