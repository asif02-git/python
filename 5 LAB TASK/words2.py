# Q16. Find longest word

sentence = "Python programming is very interesting"

words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

# OUTPUT:
# Longest word: programming