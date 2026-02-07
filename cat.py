n = int(input("Enter length: "))
file = open("data.txt", "r")

words = file.read().split()

for word in words:
    if len(word) > n:
        print(word)

file.close()
