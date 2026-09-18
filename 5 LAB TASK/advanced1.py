# Q20. Remove duplicate characters

text = "programming"

result = ""

for char in text:
    if char not in result:
        result += char

print("Original:", text)
print("Without duplicates:", result)

# OUTPUT:
# Original: programming
# Without duplicates: progamin