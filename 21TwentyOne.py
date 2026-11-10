"""Write a Python program to open a file for read operation and also handle FileNotFoundError."""
try:
    file = open("Python/example.txt", "r")
    content = file.read()
    print("File content: ")
    print(content)  
except FileNotFoundError:
    print("Error: File not found.")