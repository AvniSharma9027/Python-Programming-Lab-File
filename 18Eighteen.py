"""Write a Python program to create a function calc(a, b) that takes two numbers as input and returns 
a list containing the results of addition, subtraction, multiplication, and division of the 
two numbers."""
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
def calc(a,b):
    add = a+b
    sub = a-b 
    mul = a*b
    div = a/b if b!=0 else "undefined (division by zero)"
    return [add, sub, mul, div]
print(calc(a,b))