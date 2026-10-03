# lab1_task2.py

def simple_interest(principal, rate, time):
    """
    Calculates simple interest given principal, rate of interest per annum, and time in years.
    Formula: SI = (P * R * T) / 100
    """
    return (principal * rate * time) / 100

# Driving code / User input simulation
p = 10000.0
r = 7.5
t = 3.0

si = simple_interest(p, r, t)
print(f"Principal: ${p}, Rate: {r}%, Time: {t} years")
print(f"Calculated Simple Interest: ${si:.2f}")

OUTPUT:
# Principal: $10000.0, Rate: 7.5%, Time: 3.0 years
# Calculated Simple Interest: $2250.00
