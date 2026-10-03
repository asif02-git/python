# lab5_task1.py

counter = 0  # Global variable

def show_local():
    counter = 10  # Local variable with same name
    print(f"Inside show_local() -> Local counter: {counter}")

show_local()
print(f"Outside function     -> Global counter: {counter}")

OUTPUT:
# Inside show_local() -> Local counter: 10
# Outside function     -> Global counter: 0
