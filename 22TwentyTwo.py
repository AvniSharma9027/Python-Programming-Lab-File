"""Write a Python program to create a user-defined package containing two modules: one for performing 
addition and another for performing multiplication. Import the package in the main program and use 
the functions to add and multiply two numbers entered by the user."""
from mypackage import add, multiply
def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    sum_result = add(num1, num2)
    mul_result = multiply(num1, num2)
    print(f"Addition of {num1} and {num2}: {sum_result}")
    print(f"Multiplication of {num1} and {num2}: {mul_result}")
if __name__ == "__main__":
    main()