def multiply(num1, num2):
    result = 0
    for _ in range(abs(num2)):
        result += num1
    
    if (num1 < 0) != (num2 < 0):
        result = -result

    return result

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = multiply(num1, num2)
print("Multiplication of the two numbers without using multiplication operator:", result)