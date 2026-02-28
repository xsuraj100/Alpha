file = open("data.txt", "r")
text = file.read()
count = 0

for ch in text:
    if ch.isalpha():
        count += 1

print("Alphabets:", count)
file.close()