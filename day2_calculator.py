while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    print("ENTER CHOICE : ")
    c=int(input())
    if c!=0 and c<5:
        print("ENTER NUMBERS : ")
        a=float(input("ENTER FIRST NUMBER:"))
        b=float(input("ENTER SECOND NUMBER:"))
        if c==1:
            o=a+b
            print("THE ADDITION OF 2 NO IS:",o)
        elif c==2:
            o=a-b
            print("THE DIFFERNCE OF 2 NO IS:",o)
        elif c==3:
            o=a*b
            print("THE PRODUCT OF 2 NO IS:",o)
        else:
            if b==0:
                print("DENOMINATOR CANNOT BE ZERO!")
                B=float(input("ENTER A VALID NUMBER:"))
                b=B
            o=a/b
            print("THE DIVISION OF 2 NO IS:",o)
    elif c==5:
        print("EXITED SUCCESSFULLY")
        break
    else:
        print("GIVE A VALID OPTION>>")
    