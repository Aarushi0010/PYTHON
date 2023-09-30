# 1. using union() method [returns new set containg items of both sets]
set1 = {"aarushi" , "japleen"}
set2 = {"vivek" , "ujwal"}
set3 = set1.union(set2)
print(set3)

# 2. using update() method 
set1.update(set2)
print(set1)

# 2. intersection_update() method [keeps only the items present in both the sets]
set4 = {1 , 2 , 3 , 4 , 5}
set5 = {3 , 4 , 6 , 7}
set4.intersection_update(set5)
print(set4)

# 3. intersection() method  [returns the new set with items common to both sets]
x = set4.intersection(set5)
print(x)

# 4. symmetric_difference_update() method [returns element not common to both]
set4.symmetric_difference_update(set5)
print(set4)

# 5. symmetric_difference() method  [returns new set with elemnts not common to both sets]
y = set4.symmetric_difference(set5)
print(y)