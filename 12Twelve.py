"""Write a python program to create a list of five students by taking input from user and to 
display names of the students in ascending and descending order."""
n = int(input("Enter the number of students: "))
students = []
for i in range(n):
    name = input("Enter the name of student {}: ".format(i + 1))
    students.append(name)
print("Students in ascending order:")
for student in sorted(students):
    print(student)
print("Students in descending order:")
for student in sorted(students, reverse=True):
    print(student)