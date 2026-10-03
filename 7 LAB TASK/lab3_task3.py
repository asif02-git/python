# lab3_task3.py

def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

num = 12345
print(f"Number: {num}")
print(f"Sum of digits: {sum_of_digits(num)}")
print(f"Reversed number: {reverse_number(num)}")


OUTPUT:
# Number: 12345
# Sum of digits: 15
# Reversed number: 54321
