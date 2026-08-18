# Exercise 17

start = int(input("Enter lower limit: "))
end = int(input("Enter upper limit: "))

print("Prime numbers:")

for n in range(start, end + 1):
    if n < 2:
        continue

    prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")

# Output:
# Enter lower limit: 10
# Enter upper limit: 30
# Prime numbers:
# 11 13 17 19 23 29