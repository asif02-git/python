# lab2_task3.py

def total_marks(*marks):
    if not marks:
        return 0, 0.0
    total = sum(marks)
    avg = total / len(marks)
    return total, avg

# Testing with 3, 5, and 1 mark
for dataset in [(85, 90, 78), (92, 88, 79, 95, 84), (90,)]:
    total, avg = total_marks(*dataset)
    print(f"Marks: {dataset} -> Total: {total}, Average: {avg:.2f}")

OUTPUT:
# Marks: (85, 90, 78) -> Total: 253, Average: 84.33
# Marks: (92, 88, 79, 95, 84) -> Total: 438, Average: 87.60
# Marks: (90,) -> Total: 90, Average: 90.00