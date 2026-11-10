"""Write a Python program to take a string as input and check given string is Palindrome or not."""
str1 = input("Enter a string: ")
str2 = str1[ : :-1]
if str1 == str2:
    print("The given string is a Palindrome.")
else:
    print("The given string is not a Palindrome.")
