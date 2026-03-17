import string

file = open("data.txt", "r")
text = file.read()
count = 0

for ch in text:
    if ch in string.punctuation:
        count += 1

print("Punctuation marks:", count)
file.close()