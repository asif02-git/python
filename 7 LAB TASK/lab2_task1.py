# lab2_task1.py

def student_info(name, roll_no, branch):
    print(f"Name: {name} | Roll No: {roll_no} | Branch: {branch}")

print("Call 1 (Positional Arguments):")
student_info("Asha", 101, "CSE")

print("Call 2 (Keyword Arguments in different order):")
student_info(branch="CSE", name="Asha", roll_no=101)


OUTPUT:
# Call 1 (Positional Arguments):
# Name: Asha | Roll No: 101 | Branch: CSE
# Call 2 (Keyword Arguments in different order):
# Name: Asha | Roll No: 101 | Branch: CSE
