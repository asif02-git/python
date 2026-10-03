# lab5_task3.py

counter = 10

def faulty_increment():
    try:
        # Tries to assign without global declaration
        counter += 1
    except UnboundLocalError as e:
        print(f"Caught expected error: {e}")

def fixed_increment():
    global counter
    counter += 1
    print(f"Successfully incremented global counter to: {counter}")

faulty_increment()
fixed_increment()


OUTPUT:
# Caught expected error: local variable 'counter' referenced before assignment
# Successfully incremented global counter to: 11
