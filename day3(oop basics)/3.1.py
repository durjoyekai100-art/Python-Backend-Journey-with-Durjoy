class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def study(self):
        print(f"{self.name} is studying in grade {self.grade}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teaches(self):
        print(f"{self.name} teaches {self.subject}.")

st = Student("Durjoy", 15, "10")
te = Teacher("LKK", 18, "Physics")

st.introduce()
te.introduce()

st.study()
te.teaches()