# Q23. String to list and list to string

text = "Python"

characters = list(text)

print("String:", text)
print("List:", characters)

new_string = "".join(characters)

print("Back to string:", new_string)

# OUTPUT:
# String: Python
# List: ['P', 'y', 't', 'h', 'o', 'n']
# Back to string: Python