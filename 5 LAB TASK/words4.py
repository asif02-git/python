# Q18. Title Case without using title()

sentence = "python programming language"

words = sentence.split()

result = []

for word in words:
    result.append(word[0].upper() + word[1:])

result = " ".join(result)

print("Original:", sentence)
print("Title case:", result)

# OUTPUT:
# Original: python programming language
# Title case: Python Programming Language