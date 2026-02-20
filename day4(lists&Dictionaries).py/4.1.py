employees = [
    {"name" : "jj", "working hour" : 7},
    {"name" : "kk", "working hour" : 6},
    {"name" : "ll", "working hour" : 12}
]

employees.append({"name" : "ff", "working hour" : 13})

for emp in employees:
    print(f"{emp["name"]} works for {emp["working hour"]} hours.")
    
    if emp["working hour"] >= 10:
        print(emp["name"], "is hardworking person.")
    print()