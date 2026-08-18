# Exercise 9

n = int(input("Enter a number: "))

temp = abs(n)
sum_digits = 0
count = 0

if temp == 0:
    count = 1

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    count += 1
    temp //= 10

average = sum_digits / count

print("Sum:", sum_digits)
print("Average:", average)

# Output:
# Enter a number: 1234
# Sum: 10
# Average: 2.5