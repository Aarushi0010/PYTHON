def to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = int(input("Enter your choice (1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius): "))

if choice == 1:
    num1 = float(input("Enter temperature :"))
    x = to_fahrenheit(num1)
    print("Fahrenheit value is : " , x)

elif choice == 2:
    num2 = float(input("Enter temperature :"))
    y = to_celsius(num2)
    print("celsius value is " , y)

else :
    print("Invalid choice")
