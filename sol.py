file = open("data.txt", "r")
lines = file.readlines()

shortest = min(lines, key=len)
print("Shortest line:", shortest)

file.close()