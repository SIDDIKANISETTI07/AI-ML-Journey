class Student:
    def __init__(self, name, roll, marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll no:",self.roll)
        print("Marks:",self.marks)
    def check_pass(self):
        if self.marks>=35:
            print("Result: PASS")
        else:
            print("Result: FAIL")
s1=Student("Syam", 27, 100)
s1.display()
s1.check_pass()