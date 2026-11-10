"""Write a Python program to create a list of ten integers by taking input from the user and print
the Sum and Average of numbers."""
n = int(input("Enter the number of integers you want to input: "))
lst1 = []
for i in range(n):
    num = int(input("Enter a number: "))
    lst1.append(num)
print("Sum of the numbers is:", sum(lst1))
print("Average of the numbers is:", sum(lst1)/n)