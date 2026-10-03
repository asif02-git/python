# lab6_task1.py

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))

words = ["python", "functional", "programming"]
uppercase_words = list(map(str.upper, words))

print(f"Celsius: {celsius_temps} -> Fahrenheit: {fahrenheit_temps}")
print(f"Original Words: {words} -> Uppercase: {uppercase_words}")


OUTPUT:
# Celsius: [0, 20, 37, 100] -> Fahrenheit: [32.0, 68.0, 98.6, 212.0]
# Original Words: ['python', 'functional', 'programming'] -> Uppercase: ['PYTHON', 'FUNCTIONAL', 'PROGRAMMING']
