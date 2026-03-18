file = open("data.txt", "r")
words = file.read().split()

for word in words:
    print(word)

file.close()