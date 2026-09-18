# Q17. Reverse order of words

sentence = "I love learning Python"

words = sentence.split()

reverse_words = words[::-1]

result = " ".join(reverse_words)

print("Original:", sentence)
print("Reversed order:", result)

# OUTPUT:
# Original: I love learning Python
# Reversed order: Python learning love I