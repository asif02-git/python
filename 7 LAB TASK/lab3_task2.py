# lab3_task2.py

call_count_fib5 = 0

def fibonacci(n):
    global call_count_fib5
    if n == 5:
        call_count_fib5 += 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = [fibonacci(i) for i in range(15)]
print("First 15 Fibonacci terms:")
print(terms)

# Calculate fibonacci(10) and observe fibonacci(5) recalculations
call_count_fib5 = 0
fibonacci(10)
print(f"\nWhile calculating fibonacci(10), fibonacci(5) was computed {call_count_fib5} times.")


OUTPUT:
# First 15 Fibonacci terms:
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
# 
# While calculating fibonacci(10), fibonacci(5) was computed 8 times.