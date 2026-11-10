"""Write a Python program to create a tuple of five integers and apply len(), max(), min(), and sum() 
functions on tuple."""
t = ()
for i in range(5):
    num = int(input("Enter an integer: "))
    t += (num,)
print("Tuple:", t)
print("Length of tuple:", len(t))
print("Maximum value in tuple:", max(t))
print("Minimum value in tuple:", min(t))
print("Sum of all elements in tuple:", sum(t))