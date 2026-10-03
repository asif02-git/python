# lab1_task5.py

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def menu():
    sample_choices = [(1, 37.0), (2, 98.6), (3, None)]
    
    for choice, val in sample_choices:
        print("\n--- Temperature Converter ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        print(f"Selected Choice: {choice}")
        
        if choice == 1:
            res = celsius_to_fahrenheit(val)
            print(f"{val}°C = {res:.2f}°F")
        elif choice == 2:
            res = fahrenheit_to_celsius(val)
            print(f"{val}°F = {res:.2f}°C")
        elif choice == 3:
            print("Exiting program.")
            break

menu()

OUTPUT:
# --- Temperature Converter ---
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Exit
# Selected Choice: 1
# 37.0°C = 98.60°F

# --- Temperature Converter ---
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Exit
# Selected Choice: 2
# 98.6°F = 37.00°C

# --- Temperature Converter ---
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Exit
# Selected Choice: 3
# Exiting program.
