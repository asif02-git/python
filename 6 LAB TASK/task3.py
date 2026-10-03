import re

# 1. Hide email addresses
text = "Contact john@gmail.com or admin@yahoo.com"
hidden = re.sub(r"\b[\w.-]+@[\w.-]+\.\w+\b", "[EMAIL HIDDEN]", text)
print("Hidden emails:", hidden)

# 2. Convert Doe, John to John Doe
name = "Doe, John"
new_name = re.sub(r"(\w+),\s*(\w+)", r"\2 \1", name)
print("Changed name:", new_name)

# 3. Double every number
sentence = "I have 3 apples and 5 oranges"

def double_number(match):
    return str(int(match.group()) * 2)

result = re.sub(r"\d+", double_number, sentence)
print("Doubled numbers:", result)

# 4. Remove repeated punctuation
text2 = "Wait!!! What??? Really!!!"
result2, count = re.subn(r"([!?])\1+", r"\1", text2)
print("Cleaned text:", result2)
print("Number of replacements:", count)

# Output:
# Hidden emails: Contact [EMAIL HIDDEN] or [EMAIL HIDDEN]
# Changed name: John Doe
# Doubled numbers: I have 6 apples and 10 oranges
# Cleaned text: Wait! What? Really!
# Number of replacements: 3