n=int(input("ENTER NO OF ELEMENTS: "))
lst=[]
for i in range(1, n+1):
    lst.append(int(input(f"ENTER ELEMENT {i}: ")))
print("Largest: ",max(lst))
print("Smallest: ",min(lst))
s=0
for i in range(n):
    s+=lst[i]
print("Sum: ",s)
a=s/n
print("Average: ",a)
lst2=[]
for i in range(n):
    if lst[i]%2==0:
        lst2.append(lst[i])
print("Even numbers: ",lst2)
lst.sort()
print("Sorted ascending: ",lst)
lst.sort(reverse=True)
print("Sorted descending: ",lst)