file = open("data.txt", "r")
count = 0

for line in file:
    if line[0].isupper():
        count += 1

print("Lines starting with capital letter:", count)
file.close()