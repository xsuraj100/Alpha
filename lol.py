file = open("data.txt", "w")

for i in range(3):
    line = input("Enter line: ")
    file.write(line + "\n")

file.close()
print("Lines saved")