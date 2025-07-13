def primecheck(n):
    f=0
    for i in range(2, n):
        if n%i==0:
            f=f+1
            break
    if f>0:
        print(f"{n} is not a Prime number")
    else:
        print(f"{n} is a Prime number")
while True:
    n=int(input("ENTER NUMBER: "))
    primecheck(n)
    print("1.Check another number")
    print("2.EXIT")
    c=int(input("ENTER CHOICE: "))
    if c not in [1, 2]:#Used instead of c<1 and c>2
        c=int(input("ENTER VALID OPTION FROM MENU!: "))
    if c==2:
        print("EXITED SUCCESSFULLY!")
        break
