file = open("data.txt", "r")
words = file.read().lower().split()
count = 0

for word in words:
    if word[-1] in "aeiou":
        count += 1

print("Words ending with vowel:", count)
file.close()