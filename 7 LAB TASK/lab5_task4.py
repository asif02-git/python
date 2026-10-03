# lab5_task4.py

def make_counter():
    count = 0  # Enclosing local variable
    
    def increment():
        nonlocal count
        count += 1
        return count
        
    return increment

my_counter = make_counter()

print(f"First call : {my_counter()}")
print(f"Second call: {my_counter()}")
print(f"Third call : {my_counter()}")


OUTPUT:
# First call : 1
# Second call: 2
# Third call : 3
