def addition(num1 , num2):
    while num2!= 0:
        carry = num1 & num2 
        num1 = num1 ^ num2 
        num2 = carry << 1

    return num1
num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))

result = addition(num1 , num2)
print("sum of numbers is : " , result)