# lab1_task4.py

def stats(numbers):
    """Accepts a list of numbers and returns min, max, and average as a tuple."""
    if not numbers:
        return 0, 0, 0
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

data = [45, 12, 89, 34, 67, 23]
min_val, max_val, avg_val = stats(data)

print(f"Dataset: {data}")
print(f"Minimum Value: {min_val}")
print(f"Maximum Value: {max_val}")
print(f"Average Value: {avg_val:.2f}")


OUTPUT:
# Dataset: [45, 12, 89, 34, 67, 23]
# Minimum Value: 12
# Maximum Value: 89
# Average Value: 45.00
