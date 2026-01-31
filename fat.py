import os

filename = "sample.txt"

if not os.path.exists(filename):
    open(filename, "w").close()
    print("File created")
else:
    print("File already exists")
