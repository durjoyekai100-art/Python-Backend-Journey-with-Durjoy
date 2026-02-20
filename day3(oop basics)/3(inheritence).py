class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print("Hi, I am", self.name)
    
class Teacher(Person):
    def subject(self):
        print("I teach python")

t = Teacher("Durjoy")

t.introduce()
t.subject()