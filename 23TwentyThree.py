"""Write a Python program to create a NumPy array containing the marks of five students and display 
them as a bar chart using the Matplotlib library."""
import numpy as np
import matplotlib.pyplot as plt
students = ['S1', 'S2', 'S3', 'S4', 'S5']
marks_list = []
for student in students:
    score = float(input(f"Enter marks for {student}: "))
    marks_list.append(score)
marks = np.array(marks_list)
plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of Five Students")
plt.show()