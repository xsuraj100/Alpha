f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")

if f1.read() == f2.read():
    print("Files are identical")
else:
    print("Files are different")

f1.close()
f2.close()