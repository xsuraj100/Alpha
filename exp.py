import pickle

file = open("students.dat", "rb")
name = input("Enter name to search: ")

found = False

try:
    while True:
        data = pickle.load(file)
        if data[0] == name:
            print("Found:", data)
            found = True
except EOFError:
    file.close()

if not found:
    print("Record not found")