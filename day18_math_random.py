import math

num = float(input("Enter a number: "))
print("Square root:", math.sqrt(num))
print("Power (num^3):", math.pow(num, 3))
print("Ceil value:", math.ceil(num))
print("Floor value:", math.floor(num))
print("Sine of num:", math.sin(num))
import random

print("Random no between 1 and 10:",random.randint(1, 10))
print("Random float no between 0 and 1:",random.random())
lst=[10, 20, 30, 40]
print("Random choice from the list:",random.choice(lst))
random.shuffle(lst)
print("List after shuffleing randomly:",lst)