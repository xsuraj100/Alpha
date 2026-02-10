f1 = open("data.txt", "r")
content = f1.read()
f1.close()

f2 = open("reverse.txt", "w")
f2.write(content[::-1])
f2.close()

print("Reversed content saved")
