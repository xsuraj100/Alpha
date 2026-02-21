file = open("data.txt", "r")
text = file.read()
file.close()

text = text.replace("\n", " ")

file = open("data.txt", "w")
file.write(text)
file.close()
