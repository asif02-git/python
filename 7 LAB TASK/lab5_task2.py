# lab5_task2.py

counter = 0

def increment_counter():
    global counter
    counter += 1

for i in range(1, 6):
    increment_counter()
    print(f"Call {i}: Counter value = {counter}")


OUTPUT:
# Call 1: Counter value = 1
# Call 2: Counter value = 2
# Call 3: Counter value = 3
# Call 4: Counter value = 4
# Call 5: Counter value = 5
