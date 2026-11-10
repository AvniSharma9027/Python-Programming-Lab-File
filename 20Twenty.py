"""Write a Python program to perform division operation on two integers and also handle ValueError 
and ZeroDivisionError."""
try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Second integer cannot be zero.")