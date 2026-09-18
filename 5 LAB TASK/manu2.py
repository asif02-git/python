# Q7. Remove whitespace

text = "Hello World Python"

result = ""

for char in text:
    if not char.isspace():
        result += char

print("Original:", text)
print("Without whitespace:", result)

# OUTPUT:
# Original: Hello World Python
# Without whitespace: HelloWorldPython