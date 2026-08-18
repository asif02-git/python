# Exercise 30

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print("* " * i + "  " * (2 * (n - i)) + "* " * i)

for i in range(n - 1, 0, -1):
    print("* " * i + "  " * (2 * (n - i)) + "* " * i)

# Output:
# Enter number of rows: 4
# *             *
# * *         * *
# * * *     * * *
# * * * * * * * *
# * * *     * * *
# * *         * *
# *             *