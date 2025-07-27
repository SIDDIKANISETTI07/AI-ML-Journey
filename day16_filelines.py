with open("lines.txt", "w") as f:
    for i in range(5):
        f.write(input(f"ENTER LINE {i+1}:"))
        f.write("\n")
with open("lines.txt", "r") as f:
    flst=f.readlines()
flines=len(flst)
flong=max(flst, key=len).strip()
print("TOTAL NO OF LINES:",flines)
print("LONGEST LINE:",flong)