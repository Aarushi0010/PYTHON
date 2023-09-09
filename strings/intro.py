# we can use "" or '' to represent a string 

#assignin multiline strings to a variable using """ or '''

a = '''Hi! python is an interesting language 
    it's easy compared to other HLL 
    Learning it is always fun.'''

print(a)

#strings as arrays 
x = "banana"
print(x[2])

#looping through string 
for x in 'banana':
    print(x)

#length of string 
x = "github repository"
print(len(x))

#check for a word in a string 
txt = "the best things in life are free"
print("free" in txt)                 #boolean statement 

#uing if statement
txt = 'the best things in life are free'
if('free' in txt):
    print("yes , text is present")

#if not present in string 
x = "the best things in life are free"
if("tree" not in txt):
    print("not the right text")