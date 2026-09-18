# Q25. Implement own find() and count()

text = "banana"
character = "a"

# Own version of find()
def my_find(text, character):
    for i in range(len(text)):
        if text[i] == character:
            return i
    return -1


# Own version of count()
def my_count(text, character):
    count = 0

    for char in text:
        if char == character:
            count += 1

    return count


print("First occurrence:", my_find(text, character))
print("Number of occurrences:", my_count(text, character))

# OUTPUT:
# First occurrence: 1
# Number of occurrences: 3