"""Write a Python program to calculate the volume and surface area of a cuboid based on the given 
dimensions: length, breadth, and height. """
l = float(input("Enter the length of the cuboid: "))
b = float(input("Enter the breadth of the cuboid: "))
h = float(input("Enter the height of the cuboid: "))
v = l * b * h
sa = 2 * (l * b + b * h + h * l)
print("Volume of the cuboid:", v)
print("Surface area of the cuboid:", sa)