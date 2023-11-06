def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y 
def div(x,y):
    if y == 0:
        print("Invalid division")
    else:
        return x / y
def mod(x,y):
    if y == 0:
        print("Invalid division")
    else:
        return x % y
 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /, %): ")

if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = sub(num1, num2)
elif operation == '*':
    result = mul(num1, num2)
elif operation == '/':
    result = div(num1, num2)
elif operation == '%':
    result = mod(num1, num2)
else:
    result = "Invalid input: Operation not supported"

print("Performed output:", result)