n = int(input("Enter length: "))
file = open("data.txt", "r")

for line in file:
    if len(line) > n:
        print(line, end="")

file.close()
