class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show_info(self):
        print("Name:", self.name)
        print("Roll:", self.roll)

s1 = Student("Durjoy", 1)
s2 = Student("FJJ", 2)

s1.show_info()
s2.show_info()