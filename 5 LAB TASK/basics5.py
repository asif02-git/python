# Q5. Count vowels, consonants, digits and spaces

text = "Asif 123"

vowels = 0
consonants = 0
digits = 0
spaces = 0

for char in text:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)

# OUTPUT:
# Vowels: 2
# Consonants: 2
# Digits: 3
# Spaces: 1