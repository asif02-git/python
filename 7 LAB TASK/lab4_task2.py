# lab4_task2.py

grade = lambda marks: 'Pass' if marks >= 40 else 'Fail'

marks_list = [75, 32, 40, 88, 29, 95]
for m in marks_list:
    print(f"Marks: {m} -> Status: {grade(m)}")


OUTPUT:
# Marks: 75 -> Status: Pass
# Marks: 32 -> Status: Fail
# Marks: 40 -> Status: Pass
# Marks: 88 -> Status: Pass
# Marks: 29 -> Status: Fail
# Marks: 95 -> Status: Pass
