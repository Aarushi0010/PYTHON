# Assigning of values to a tuple is called packing a tuple

fruits = ("apple", "banana", "cherry")

# we can also extract the values back into the variable 
fruits = ("apple", "banana", "cherry")
(green , yellow , red ) = fruits
print (green)
print (yellow)
print (red) 

# using asterik
fruits = ("apple", "banana", "cherry" , "grapes" , "pineapple")
( green , yellow , *red ) = fruits 
print (green)
print (yellow)
print (red)
