# lab4_task4.py

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cubes = list(map(lambda x: x ** 3, numbers))
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))

print(f"Original List: {numbers}")
print(f"Cubes: {cubes}")
print(f"Divisible by 3: {divisible_by_3}")


OUTPUT:
# Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Cubes: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# Divisible by 3: [3, 6, 9]
