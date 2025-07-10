while True:
    print("ENTER NUMBER : ")
    n=int(input())
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")
    s=n*n
    print("THE SQUARE OF THE NO IS : ",s)
    print("1.GIVE ANOTHER NUMBER")
    print("2.EXIT")
    print("ENTER OPTION")
    o=int(input())
    if o==2:
        print("EXITED")
        break
