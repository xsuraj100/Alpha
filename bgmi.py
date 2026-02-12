f1 = open("data.txt", "r")
f2 = open("numbered.txt", "w")

for i, line in enumerate(f1, start=1):
    f2.write(str(i) + ". " + line)

f1.close()
f2.close()
