s=input("ENTER STRING: ")
rev=s[::-1]
vowels='aeiouAEIOU'
vc=0
cc=0
for char in s:
    if char in vowels:
        vc += 1
    else:
        cc += 1
if s==rev:
    pal='Yes'
else:
    pal='No'
print("Original :",s)
print("Reversed :",rev)
print("Length :",len(s))
print("No of vowels :",vc)
print("No of consonants :",cc)
print("Palindrome :",pl)