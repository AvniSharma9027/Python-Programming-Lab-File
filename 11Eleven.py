"""Write a Python program to create a list of ten integers by taking input from the user and check
whether a given number is present in the list or not."""
n = int(input("Enter the number of integers you want to input: "))
lst1 = []
for i in range(n):
    num = int(input("Enter a number: "))
    lst1.append(num)
num = int(input("Enter a number to check: "))
if num in lst1:
    print(num,"is present in the list.")
else:
    print(num,"is not present in the list.")