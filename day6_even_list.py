lst=[]
for i in range(1, 11):
    lst.append(int(input(f"ENTER ELEMENT {i}: ")))
for i in range(0, 10):
    if lst[i]%2==0:
        print(lst[i],end=" ")