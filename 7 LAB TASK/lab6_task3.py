# lab6_task3.py

from functools import reduce

nums = [2, 3, 4, 5]

product = reduce(lambda x, y: x * y, nums)
max_val = reduce(lambda a, b: a if a > b else b, nums)

words = ["Functional", "Programming", "in", "Python"]
sentence = reduce(lambda a, b: a + " " + b, words)

print(f"Product of {nums}: {product}")
print(f"Max value of {nums}: {max_val}")
print(f"Concatenated Sentence: '{sentence}'")


OUTPUT:
# Product of [2, 3, 4, 5]: 120
# Max value of [2, 3, 4, 5]: 5
# Concatenated Sentence: 'Functional Programming in Python'
