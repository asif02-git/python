# Exercise 10

n = int(input("Enter an integer: "))

sign = -1 if n < 0 else 1
n = abs(n)

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

reverse *= sign

print("Reverse:", reverse)

# Output:
# Enter an integer: 1234
# Reverse: 4321