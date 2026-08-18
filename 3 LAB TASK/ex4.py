# Exercise 4

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

print("Largest number:", largest)

# Output:
# Enter first number: 25
# Enter second number: 40
# Enter third number: 30
# Largest number: 40