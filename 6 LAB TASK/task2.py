import re

text = "NASA and USA are working with ISRO on SPACE research"

# Find all capital words
capital_words = re.findall(r"\b[A-Z]{2,}\b", text)
print("Capital words:", capital_words)

# Find words longer than 6 characters
print("Long words:")
for match in re.finditer(r"\b[A-Za-z]{7,}\b", text):
    print(match.group(), match.start())

# Find dollar amounts
prices = "apples: $3.50, bananas: $1.20, mango: $4.75"
amounts = re.findall(r"\$\d+\.\d+", prices)
print("Dollar amounts:", amounts)

# Count occurrences
print("Number of dollar amounts:", len(amounts))

# Output:
# Capital words: ['NASA', 'USA', 'ISRO', 'SPACE']
# Long words:
# working 13
# research 44
# Dollar amounts: ['$3.50', '$1.20', '$4.75']
# Number of dollar amounts: 3