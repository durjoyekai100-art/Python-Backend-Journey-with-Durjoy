Employees = [
    {"name" : "Durjoy", "salary" : 100000},
    {"name" : "LL", "salary" : 120000},
    {"name" : "ii", "salary" : 60000}

]

for employee in Employees:
    print("___EMPLOYEE DETAILS___")
    print(f"{employee["name"]} earns {employee["salary"]}")
     # add spaces under lines

    if employee["salary"] >= 100000:
        
        print(f"{employee["name"]} is Grade A Level Employee")
        print() # adds space under section