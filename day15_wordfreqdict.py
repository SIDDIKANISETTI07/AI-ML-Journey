sen = input("Enter a sentence:")
words = sen.split()
print(words)
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print("\nWord Frequencies:")
for word, count in freq.items():
    print(f"{word} : {count}")