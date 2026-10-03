# lab1_task3.py

def is_even(n):
    """Returns True if n is even, False otherwise."""
    return n % 2 == 0

# Driver program with sample inputs
numbers = [12, 7, 0, 15, 22]

for num in numbers:
    if is_even(num):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")


OUTPUT:
# 12 is Even
# 7 is Odd
# 0 is Even
# 15 is Odd
# 22 is Even
