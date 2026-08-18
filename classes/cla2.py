# LAB 07 - Task 2
# Add two numbers using command-line arguments

import sys

if len(sys.argv) != 3:
    print("Usage: python add.py <num1> <num2>")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Sum =", num1 + num2)

# Run:
# python add.py 10 20

# Output:
# Sum = 30