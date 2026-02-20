class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12
    
e1 = Employee("DD", 5000)
e2 = Employee("FF", 3000)

print(e1.name, "yearly salary = ", e1.annual_salary())
print(e2.name, "yearly salary = ", e2.annual_salary())

