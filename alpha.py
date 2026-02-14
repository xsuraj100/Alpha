file = open("data.txt", "r")
text = file.read()

print("Number of commas:", text.count(","))

file.close()
