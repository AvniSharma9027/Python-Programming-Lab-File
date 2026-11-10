"""Create a window having two radio button, one label with male and second with Female and create a 
button and call a function name show_msg() which displays a message using messageBox."""
import tkinter as tk
from tkinter import messagebox
def show_msg():
    messagebox.showinfo("Message", "Gender selected: " + gender.get())
root = tk.Tk()
root.geometry("300x200")
gender = tk.StringVar(value=" ")
tk.Label(root, text="Select Gender").pack()
tk.Radiobutton(root, text="Female", variable=gender, value="Female").pack()
tk.Radiobutton(root, text="Male", variable=gender, value="Male").pack()
tk.Button(root, text="Submit", command=show_msg).pack()
root.mainloop()