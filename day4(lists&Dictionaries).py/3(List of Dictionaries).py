students = [
    {"name": "Durjoy", "roll": 4, "cgpa": 3.3},
    {"name": "kk", "roll": 2, "cgpa": 2.44},
    {"name": "kl", "roll": 5, "cgpa": 4}
]

for student in students:
    print("___student___")
    for key, value in student.items(): # that's the standard level of code
        print(f"{key:>8} : {value}")
    print()