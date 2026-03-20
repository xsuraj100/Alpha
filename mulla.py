file = open("data.txt", "r")
words = file.read().split()

for word in words:
    if len(word) > 5:
        print(word)

file.close()