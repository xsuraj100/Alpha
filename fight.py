import pickle

file = open("students.dat", "wb")

for i in range(3):
    name = input("Name: ")
    marks = int(input("Marks: "))
    pickle.dump((name, marks), file)

file.close()