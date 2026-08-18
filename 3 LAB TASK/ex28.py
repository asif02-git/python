# Exercise 28

n = int(input("Enter number of rows: "))

for i in range(n):
    print(" " * (n - i - 1) + "*" * (i + 1))

for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (i + 1))

# Output:
# Enter number of rows: 4
#    *
#   **
#  ***
# ****
#  ***
#   **
#    *