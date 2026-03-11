file = open("data.txt", "r")
text = file.read()
file.close()

file = open("data.txt", "w")
file.write(text.lower())
file.close()

print("Converted to lowercase")