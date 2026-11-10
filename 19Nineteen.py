"""Write a Python program that imports a module mycalc and uses its functions to perform basic 
arithmetic operations: addition, subtraction, multiplication, and division. The program should take 
two numbers as input and print the results of each operation."""
import mycalc
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Addition: {mycalc.add(num1, num2)}")
print(f"Subtraction: {mycalc.subtract(num1, num2)}")
print(f"Multiplication: {mycalc.multiply(num1, num2)}")
print(f"Division: {mycalc.divide(num1, num2)}")