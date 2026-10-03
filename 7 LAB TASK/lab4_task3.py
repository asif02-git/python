# lab4_task3.py

students = [("Ravi", 78), ("Sita", 92), ("Amit", 65)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print(f"Sorted students by marks (descending): {sorted_students}")

words = ["apple", "banana", "kiwi", "dragonfruit", "fig"]
sorted_words = sorted(words, key=lambda w: len(w))
print(f"Sorted words by length: {sorted_words}")


OUTPUT:
# Sorted students by marks (descending): [('Sita', 92), ('Ravi', 78), ('Amit', 65)]
# Sorted words by length: ['kiwi', 'apple', 'banana', 'fig', 'dragonfruit']
