word = input("Enter word: ")
file = open("data.txt", "r")

for line in file:
    if word in line:
        print(line, end="")

file.close()
