import math 
def calculate_square_root(num): 
 return math.sqrt(num) 
def calculate_power(base, exponent): 
 return base ** exponent 
def calculate_factorial(num): 
 return math.factorial(num) 
num = float(input("Enter a number: ")) 
choice = int(input("Enter your choice (1 for Square Root, 2 for Power, 3 for Factorial): ")) 
if choice == 1: 
 result = calculate_square_root(num) 
 print(f"The square root of {num} is {result}") 
elif choice == 2: 
 exponent = float(input("Enter the exponent: ")) 
 result = calculate_power(num, exponent) 
 print(f"{num} raised to the power of {exponent} is {result}") 
elif choice == 3: 
 if num < 0 or num != int(num): 
   print("Invalid input for factorial") 
 else: 
   result = calculate_factorial(int(num)) 
   print(f"The factorial of {num} is {result}") 
else: 
 print("Invalid user choice")