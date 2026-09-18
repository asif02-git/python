# Q6. Dictionary methods

student = {
    "name": "Asif",
    "age": 20,
    "course": "CSE"
}

print("Keys:")
for key in student.keys():
    print(key)

print("Values:")
for value in student.values():
    print(value)

print("Key-Value pairs:")
for key, value in student.items():
    print(key, ":", value)

# OUTPUT:
# Keys:
# name
# age
# course
# Values:
# Asif
# 20
# CSE
# Key-Value pairs:
# name : Asif
# age : 20
# course : CSE