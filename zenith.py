file = open("data.txt", "r")
text = file.read()
file.close()

encrypted = ""

for ch in text:
    encrypted += chr(ord(ch) + 1)

file = open("encrypted.txt", "w")
file.write(encrypted)
file.close()

print("File encrypted")