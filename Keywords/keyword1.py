# LAB 02 - Task 1
# Print the total number of Python keywords and the full list

import keyword

print("Total number of keywords:", len(keyword.kwlist))
print("List of keywords:")
print(keyword.kwlist)

# Output:
# Total number of keywords: 35   (May vary depending on Python version)
# List of keywords:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async',
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
# 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']