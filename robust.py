for i in range(1, 6):
    file = open(f"file{i}.txt", "w")
    file.write("This is file number " + str(i))
    file.close()

print("5 files created")