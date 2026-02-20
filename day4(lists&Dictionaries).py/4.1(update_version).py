employees = [
    {"name" : "jj", "working hour" : 7},
    {"name" : "kk", "working hour" : 6},
    {"name" : "ll", "working hour" : 12}
]

employees.append({"name" : "ff", "working hour" : 13})

print("WORKING HOURS REPORT")
print("*" * 35)

for emp in employees:
    name = emp["name"]
    hours = emp["working hour"] 
    print(f"{name} works for {hours} hours")

    if hours >= 10:
        print(f"{name} is a hardworking person.")
    print()
print("*" * 35)