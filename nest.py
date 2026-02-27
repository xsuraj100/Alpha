file = open("data.txt", "r")
words = file.read().split()

for word in words:
    if word.isupper():
        print(word)

file.close()