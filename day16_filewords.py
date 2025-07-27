s=input("ENTER LINE: ")
with open("sample.txt", "w") as f:
    f.write(s)
with open("sample.txt", "r") as f:
    fline=f.read()
    fwords=fline.split()
freq={}
for word in fwords:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print("Word frequencies:")
for word,count in freq.items():
    print(f"{word} : {count}")