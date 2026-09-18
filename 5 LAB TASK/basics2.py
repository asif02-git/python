# Q2. Reverse a string

text = "Asif"

# Without slicing
reverse1 = ""
for char in text:
    reverse1 = char + reverse1

# With slicing
reverse2 = text[::-1]

print("Original string:", text)
print("Without slicing:", reverse1)
print("With slicing:", reverse2)

# OUTPUT:
# Original string: Asif
# Without slicing: fisA
# With slicing: fisA