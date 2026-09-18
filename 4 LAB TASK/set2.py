# Q2. Creating sets from a list and string

my_list = [10, 20, 30, 20, 10]
my_string = "hello"

set_from_list = set(my_list)
set_from_string = set(my_string)

print("Set from list:", sorted(set_from_list))
print("Set from string:", sorted(set_from_string))

# OUTPUT:
# Set from list: [10, 20, 30]
# Set from string: ['e', 'h', 'l', 'o']