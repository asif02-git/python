# LAB 03 - Task 3(a)
# Swap using a temporary variable

a = 10
b = 20

print("Before Swapping:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After Swapping:")
print("a =", a)
print("b =", b)

# Output:
# Before Swapping:
# a = 10
# b = 20
# After Swapping:
# a = 20
# b = 10