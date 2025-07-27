students = {}

for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks for {name}: "))
    students[name] = marks

print("\nAll Student Names:")
for name in students.keys():
    print(name)

print("\nAll Marks:")
for marks in students.values():
    print(marks)
    
high = max(students, key=students.get)
print(f"\nHighest Scorer: {high} with {students[high]} marks")
