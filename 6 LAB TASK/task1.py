import re

text = "1024 requests were served in 3 seconds"

# 1. Check whether the sentence starts with a digit
m1 = re.match(r"\d", text)

# 2. Find the word "served"
m2 = re.search(r"served", text)

# 3. Check whether "12345" contains only digits
m3 = re.fullmatch(r"\d+", "12345")

# 4. Test "123a5"
m4 = re.fullmatch(r"\d+", "123a5")

print("Starts with digit:", bool(m1))
print("served position:", m2.span())
print("12345 contains only digits:", bool(m3))
print("123a5 contains only digits:", bool(m4))

# Output:
# Starts with digit: True
# served position: (22, 28)
# 12345 contains only digits: True
# 123a5 contains only digits: False