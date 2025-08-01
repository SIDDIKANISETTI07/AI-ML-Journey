import json

class Student:
    def __init__(self, name, roll, marks):
        self.n=name
        self.r=roll
        self.m=marks
    def __str__(self):
        return f"Roll Number:{self.r}, Name:{self.n}, Marks:{self.m}"
students=[]

def studentlst():
    if not students:
        print("NO students records are avaliable!")
        return
    print("list of students:")
    for s in students:
        print(s)

def search():
    try:
        r=int(input("Enter roll number to search:"))
        for s in students:
            if s.r==r:
                print("Record found")
                print(f"Name: {s.n}\nRoll number: {s.r}\nMarks: ")
                for sub, mark in s.m.items():
                    print(f" {sub} : {mark}")
                return
        print("Not found!")
    except ValueError:
        print("Invalid input enter correct roll number!")

def delete():
    try:
        r=int(input("Enter roll number to delete:"))
        for s in students:
            if s.r==r:
                students.remove(s)
                print("Student deleted successfully!")
                return
        print("Student not found!")
    except ValueError:
        print("Invalid input enter valid roll number!")

def save_file():
    with open("students.txt", "w") as f:
        json.dump([s.__dict__ for s in students], f)
    print("Student data saved to file")

def load_file():
    try:
        with open("students.txt", "r") as f:
            data =json.load(f)
            for s in data:
                students.append(Student(s['n'], s['r'], s['m']))
        print("Student data loaded from file")
    except FileNotFoundError:
        print("No data file found!")
    except json.decoder.JSONDecodeError:
        print("File is empty or corrupted!")

def menu():
    load_file()
    while True:
        print("-- MENU --")
        print("1.Add Student")
        print("2.View all Students")
        print("3.Search by roll number")
        print("4.Delete a record")
        print("5.Save to file")
        print("6.load from file")
        print("7.EXIT!")
        c=int(input("ENTER CHOICE:"))
        if c==0 or c>7:
            c=int(input("ENTER VALID OPTION FROM MENU:"))
            continue
        if c==7:
            print("EXITED SUCCESSFULLY!")
            break
        if c==1:
            try:
                name=input("Enter name:")
                roll=int(input("Enter roll number:"))
                for s in students:
                    if s.r==roll:
                        print("Roll number already exits!")
                        return
                marks={}
                s=int(input("Enter no of subjects:"))
                for _ in range(s):
                    sub=input("Enter subject name:")
                    mark=int(input(f"Enter marks in {sub}:"))
                    marks[sub]=mark
                student=Student(name, roll, marks)
                students.append(student)
                print("Student added succesfully!")
            except ValueError:
               print("Inavalid input enter correct values!")
        elif c==2:
            studentlst()
        elif c==3:
            search()
        elif c==4:
            delete()
        elif c==5:
            save_file()
        elif c==6:
            load_file()
menu()