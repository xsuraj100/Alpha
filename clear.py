file = open("data.txt", "r")
lines = file.readlines()
file.close()

freq = {}

for line in lines:
    freq[line] = freq.get(line, 0) + 1

print(freq)