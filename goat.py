file = open("data.txt", "r")

for i, line in enumerate(file):
    if i % 2 == 0:
        print(line, end="")

file.close()
