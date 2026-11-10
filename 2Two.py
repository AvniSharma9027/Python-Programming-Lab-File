"""Write a Python program that takes two numbers as input from the user and calculates the 
following operations: addition, subtraction, multiplication, and division."""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
add = num1 + num2
sub = num1 - num2
mul = num1 * num2   
div = num1 / num2 if num2 != 0 else "undefined (division by zero)"
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
