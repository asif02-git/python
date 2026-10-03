# lab3_task1.py

def factorial_recursive(n):
    if n < 0:
        return "Invalid input (Negative number)"
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    if n < 0:
        return "Invalid input"
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

n = 5
print(f"Recursive Factorial({n}): {factorial_recursive(n)}")
print(f"Iterative Factorial({n}): {factorial_iterative(n)}")
print(f"Base/Edge Case Factorial(0): {factorial_recursive(0)}")
print(f"Negative Case Factorial(-3): {factorial_recursive(-3)}")


OUTPUT:
# Recursive Factorial(5): 120
# Iterative Factorial(5): 120
# Base/Edge Case Factorial(0): 1
# Negative Case Factorial(-3): Invalid input (Negative number)