#will print boolean values : True or False
print(10>8)

print(bool("hello"))
print(bool(0))

#defining a function that will print a boolean value 
def myfunction():
    return True

print (myfunction())
print(bool(myfunction()))

#using a built-in function that prints a boolean value 
#the function is called - isinstance()

x= 200
print(isinstance(x ,int))

#or

y = []                    #an empty list
print(isinstance(y,int))