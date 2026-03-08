word = input("Enter word: ")
file = open("data.txt", "r")
count = 0

for line in file:
    if word in line:
        count += 1

print("Lines containing word:", count)
file.close()