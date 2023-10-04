# Function to add 2 numbers 
def add(x,y):
    return x + y

# Function to subtract 2 numbers
def sub(x,y):
    return x - y

# Function to multiply 2 numbers 
def mul(x,y):
    return x * y

# Function to divide 2 numbers 
def div(x,y):
    return x / y

print("SELECT OPTIONS : ")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

while True:
    choice = input("Enter choice (1/2/3/4) : ")

    if choice in ("1" , "2" , "3" , "4"):
        try:
            num1 = float(input("Enter first number :"))
            num2 = float(input("Enter second number :"))

        except ValueError:
            print("Invalid Input! Please enter numbers.")

        if choice == "1":
            print(num1, "+" , num2 , "=" , add(num1 , num2))

        if choice == "2":
            print(num1, "-" , num2, "=" ,sub(num1,num2))

        if choice == "3":
            print(num1, "*", num2, "=" , mul(num1,num2))

        if choice == "4":
            print(num1, "/" , num2, "=" , div(num1,num2))

        next_calculation = input("Want to do next calculation ? (yes/no): ")    
        if next_calculation == "no":
           break
    else:
        print("Invalid Option")
