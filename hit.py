import string

file = open("data.txt", "r")
text = file.read()
file.close()

for ch in string.punctuation:
    text = text.replace(ch, "")

file = open("data.txt", "w")
file.write(text)
file.close()

print("Punctuation removed")
