# Q2. Different data types in a list

data = [10, 3.14, "Asif", True, [1, 2, 3]]

for element in data:
    print(element, "->", type(element))

# OUTPUT:
# 10 -> <class 'int'>
# 3.14 -> <class 'float'>
# Asif -> <class 'str'>
# True -> <class 'bool'>
# [1, 2, 3] -> <class 'list'>