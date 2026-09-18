# Q21. Check string type

text = "Python123"

if text.isdigit():
    print("The string contains only digits")
elif text.isalpha():
    print("The string contains only alphabets")
elif text.isalnum():
    print("The string is alphanumeric")
else:
    print("The string contains special characters")

# OUTPUT:
# The string is alphanumeric