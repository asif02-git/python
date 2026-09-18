# Q3. Adding elements to a set

numbers = {10, 20, 30}

numbers.add(40)
print("After add():", sorted(numbers))

numbers.update([50, 60, 70])
print("After update():", sorted(numbers))

# OUTPUT:
# After add(): [10, 20, 30, 40]
# After update(): [10, 20, 30, 40, 50, 60, 70]