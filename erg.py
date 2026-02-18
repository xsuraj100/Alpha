file = open("data.txt", "r")
count = 0

for line in file:
    if line.strip() == "":
        count += 1

print("Blank lines:", count)
file.close()
