file = open("data.txt", "r")
words = file.read().split()
file.close()

freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

for w in freq:
    if freq[w] > 1:
        print(w)