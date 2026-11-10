"""Write a Python program that defines two functions: 
• area(l, b) to calculate the area of a rectangle 
• peri(l, b) to calculate the perimeter of a rectangle  
and accept  the length and breadth of the rectangle from the user and compute the area and 
perimeter using these functions."""
def area(l,b):
    Area=l*b
    print("Area of Rectangle is:",Area)
def peri(l,b):
    Peri=2*(l+b)
    print("Perimeter of Rectangle is:",Peri)
l=int(input("Enter Length: "))
b=int(input("Enter Breadth: "))
area(l,b)
peri(l,b)