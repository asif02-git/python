# Q3. Conversion between list and tuple

my_list = [10, 20, 30]
my_tuple = tuple(my_list)

print("List:", my_list)
print("Tuple:", my_tuple)

new_list = list(my_tuple)

print("Converted list:", new_list)

# OUTPUT:
# List: [10, 20, 30]
# Tuple: (10, 20, 30)
# Converted list: [10, 20, 30]