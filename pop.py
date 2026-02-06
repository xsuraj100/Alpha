file = open("data.txt", "r")
text = file.read()

tabs = text.count("\t")
print("Number of tabs:", tabs)

file.close()
