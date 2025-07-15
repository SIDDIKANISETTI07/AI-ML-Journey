n=int(input("ENTER NO OF ELEMENTS: "))
lst=[]
for i in range(1, n+1):
    lst.append(int(input(f"ENTER ELEMENT {i}: ")))
max=lst[0]
min=lst[0]
for i in range(0, n):
    if lst[i]>max:
        max=lst[i]
    if lst[i]<min:
        min=lst[i]
print("Largest: ",max)
print("Smallest: ",min)