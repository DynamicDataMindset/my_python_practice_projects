# This is a program of a simple calculator that does addition, subtraction, multiplication and Division!

print("This is a program of a simple calculator that does addition, subtraction, multiplication and Division!")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

calculate1 = num1 + num2
print(f"The addition of your two numbers is: {calculate1}")

calculate2 = num1 - num2
print(f"The Subtraction of your two numbers is: {calculate2}")

calculate3 = num1 * num2
print(f"The Multiplication of your two numbers is: {calculate3}")

if num2 != 0:
    calculate4 = num1 / num2
    print(f"The Devision of your two numbers is: {calculate4}")
else:
    print(f"Error!! Division by 0 is not allowed")
    
    








