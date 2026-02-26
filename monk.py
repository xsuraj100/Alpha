file = open("data.txt", "r")

for line in file:
    if line.strip().endswith("."):
        print(line, end="")

file.close()