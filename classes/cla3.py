# LAB 07 - Task 3
# Print script name and argument count

import sys

print("Script Name:", sys.argv[0])
print("Total Arguments:", len(sys.argv) - 1)

# Run:
# python demo.py apple banana

# Output:
# Script Name: demo.py
# Total Arguments: 2