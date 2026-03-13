file = open("data.txt", "r")
lines = file.readlines()

for line in lines[::-1]:
    print(line, end="")

file.close()