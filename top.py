file = open("encrypted.txt", "r")
text = file.read()
file.close()

decrypted = ""

for ch in text:
    decrypted += chr(ord(ch) - 1)

file = open("decrypted.txt", "w")
file.write(decrypted)
file.close()

print("File decrypted")