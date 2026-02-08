file = open("data.txt", "r")
words = file.read().split()

smallest = min(words, key=len)
print("Smallest word:", smallest)

file.close()
