import re

# 1. Valid Python variable name
pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"

names = ["_count2", "2fast", "total_sum"]

for name in names:
    if re.fullmatch(pattern, name):
        print(name, "-> Valid")
    else:
        print(name, "-> Invalid")

# 2. Find cat, dog or bird as whole words
text = "I have a cat, a dog and a bird as pets."
animals = re.findall(r"\b(cat|dog|bird)\b", text)
print("Animals:", animals)

# 3. Match hexadecimal color codes
colors = ["#FFAA00", "#000", "#12345", "#GGG"]

pattern2 = r"^#[0-9A-Fa-f]{3}([0-9A-Fa-f]{3})?$"

for color in colors:
    if re.fullmatch(pattern2, color):
        print(color, "-> Valid color")
    else:
        print(color, "-> Invalid color")

# 4. Parse a log line using named groups
log = "2024-06-01 08:15:32 ERROR Disk full"

pattern3 = (
    r"(?P<date>\d{4}-\d{2}-\d{2}) "
    r"(?P<time>\d{2}:\d{2}:\d{2}) "
    r"(?P<level>\w+) "
    r"(?P<message>.*)"
)

match = re.search(pattern3, log)

print("Date:", match.group("date"))
print("Time:", match.group("time"))
print("Level:", match.group("level"))
print("Message:", match.group("message"))

# Output:
# _count2 -> Valid
# 2fast -> Invalid
# total_sum -> Valid
# Animals: ['cat', 'dog', 'bird']
# #FFAA00 -> Valid color
# #000 -> Valid color
# #12345 -> Invalid color
# #GGG -> Invalid color
# Date: 2024-06-01
# Time: 08:15:32
# Level: ERROR
# Message: Disk full