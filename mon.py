import pickle

file = open("students.dat", "rb")

try:
    while True:
        data = pickle.load(file)
        print(data)
except EOFError:
    file.close()