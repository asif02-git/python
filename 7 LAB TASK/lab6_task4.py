# lab6_task4.py

from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Pipeline approach
evens = filter(lambda x: x % 2 == 0, nums)
squares = map(lambda x: x ** 2, evens)
total_pipeline = reduce(lambda a, b: a + b, squares)

# 2. Comprehension approach
total_comp = sum([x ** 2 for x in nums if x % 2 == 0])

print(f"Pipeline Result: {total_pipeline}")
print(f"Comprehension Result: {total_comp}")


OUTPUT:
# Pipeline Result: 220
# Comprehension Result: 220
