# Q8. Checking dictionary key

student = {
    "name": "Asif",
    "age": 20,
    "course": "CSE"
}

key = "age"

if key in student:
    print("Key exists")
    print("Value:", student[key])
else:
    print("Key does not exist")

# OUTPUT:
# Key exists
# Value: 20