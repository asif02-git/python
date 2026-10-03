# lab3_task4.py

def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)

print(f"2^3  = {power(2, 3)}")
print(f"5^0  = {power(5, 0)}")
print(f"2^-3 = {power(2, -3)}")

OUTPUT:
# 2^3  = 8
# 5^0  = 1
# 2^-3 = 0.125
