# lab6_task2.py

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(1, 51))
prime_numbers = list(filter(is_prime, numbers))

word_list = ["madam", "python", "racecar", "radar", "hello"]
palindromes = list(filter(lambda w: w == w[::-1], word_list))

print(f"Primes between 1 and 50: {prime_numbers}")
print(f"Palindromes: {palindromes}")


OUTPUT:
# Primes between 1 and 50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# Palindromes: ['madam', 'racecar', 'radar']
