def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if b!=0:
        return a/b
    else:
        return "ERROR! Denominator can't be zero"
while True:
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.EXIT")
    c=int(input("ENTER CHOICE: "))
    if c==5:
        print("EXITED SUCCESSFULLY!")
        break
    if c==0 or c>5:
       c=int(input("ENTER VALID OPTION(1-5): "))
       continue
    print("ENTER TWO NUMBERS: ")
    a=int(input())
    b=int(input())
    if c==1:
        r=add(a, b)
    elif c==2:
        r=sub(a, b)
    elif c==3:
        r=mul(a ,b)
    elif c==4:
        r=div(a, b)
    print("RESULT : ",r)