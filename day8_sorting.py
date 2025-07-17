n=int(input("ENTER NO OF ELEMENTS: "))
lst=[]
for i in range(n):
    lst.append(int(input(f"ENTER ELEMENT {i}: ")))
lst2=lst.copy()
for i in range(n):
    for j in range(0, n-i-1):
        if lst2[j+1]<lst2[j]:
            lst2[j], lst2[j+1]=lst2[j+1], lst2[j]
print("Sorted ascending: ",lst2)
lst3=lst.copy()
for i in range(n):
    for j in range(0, n-i-1):
        if lst2[j+1]>lst2[j]:
            lst2[j], lst2[j+1]=lst2[j+1], lst2[j]
print("Sorted descending: ",lst2)