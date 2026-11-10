"""Write a Python program to take a sentence as input and Count the number of words in the given 
sentence."""
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words) 
print("The number of words in the given sentence is:", word_count)