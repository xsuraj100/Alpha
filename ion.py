import string

file = open("data.txt", "r")
text = file.read()

count = 0
for ch in text:
    if ch in string.printable:
        count += 1

print("Printable characters:", count)
file.close()
