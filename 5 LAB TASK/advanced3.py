# Q22. Find duplicate characters and counts

text = "programming"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Duplicate characters:")

for char, count in frequency.items():
    if count > 1:
        print(char, ":", count)

# OUTPUT:
# Duplicate characters:
# r : 2
# g : 2
# m : 2