"""Write a Python program to find a Greatest number in given three integers."""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>b and a>c:
    print("The greatest number is:", a)
elif b>a and b>c:
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)