# lab4_task1.py

square = lambda x: x ** 2
is_even = lambda x: x % 2 == 0
larger = lambda a, b: a if a > b else b

print(f"Square of 6: {square(6)}")
print(f"Is 8 even? {is_even(8)}")
print(f"Is 7 even? {is_even(7)}")
print(f"Larger of 14 and 29: {larger(14, 29)}")


OUTPUT:
# Square of 6: 36
# Is 8 even? True
# Is 7 even? False
# Larger of 14 and 29: 29
