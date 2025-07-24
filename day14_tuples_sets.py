n=int(input("ENTER NO OF ELE: "))
lst=[]
for i in range(n):
    lst.append(int(input(f"ENTER ELE {i}: ")))
t=tuple(lst)
print("Original tuple:",t)
print("Maximum:",max(lst))
print("Minimum:",min(lst))
print("Reversed:",tuple(lst[::-1]))
s=set(t)
print("Set from tuple:",s)
a=int(input("ENTER NO TO ADD TO SET:"))
s.add(a)
print(f"After adding {a}:",s)
lst2=[]
n2=int(input("ENTER NO OF ELE FOR 2ND SET:"))
for i in range(n2):
    lst2.append(int(input(f"ENTER ELE {i}:")))
s2=set(lst2)
print("Second set:",s2)
print("Union:",s.union(s2))
print("Intersection:",s.intersection(s2))
print("Difference:",s.difference(s2))