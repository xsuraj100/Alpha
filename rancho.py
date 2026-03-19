file = open("data.txt", "r")
lines = file.readlines()
file.close()

unique_lines = set(lines)

file = open("data.txt", "w")
for line in unique_lines:
    file.write(line)

file.close()
print("Duplicate lines removed")