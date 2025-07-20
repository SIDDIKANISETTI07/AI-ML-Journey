def is_even(n):
    return n%2==0
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n //= 10
    return rev
def palindrome(n):
    return n==reverse(n)
def gcd(a, b):
    while b:
        a, b =b, a%b
    return a
while True:
    print("1.Even number check\n2.Factorial\n3.Reverse of number\n4.Palindrome check\n5.GCD of two numbers\n6.EXIT")
    c=int(input("ENTER CHOICE: "))
    if c==0 or c>6:
        print("ENTER VALID OPTION!")
        continue
    if c>0 and c<5:
        n=int(input("ENTER NUMBER: "))
    if c==1:
        print(is_even(n))
    elif c==2:
        print(fact(n))
    elif c==3:
        print(reverse(n))
    elif c==4:
        print(palindrome(n))
    elif c==5:
        a=int(input("ENTER 1 ST NUMBER: "))
        b=int(input("ENTER 2 ND NUMBER: "))
        print(gcd(a, b))
    else:
        print("EXITED SUCCESSFULLY!")
        break