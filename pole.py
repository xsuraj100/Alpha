import os

output = open("all_files.txt", "w")

for file in os.listdir():
    if file.endswith(".txt") and file != "all_files.txt":
        f = open(file, "r")
        output.write(f.read() + "\n")
        f.close()

output.close()
print("All text files merged")