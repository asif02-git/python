# LAB 02 - Task 2
# Check whether a word is a Python keyword

import keyword

word = input("Enter a word: ")

if keyword.iskeyword(word):
    print(word, "is a Python keyword.")
else:
    print(word, "is NOT a Python keyword.")

# Sample Output:
# Enter a word: for
# for is a Python keyword.

# Sample Output:
# Enter a word: hello
# hello is NOT a Python keyword.