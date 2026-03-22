import pickle

data = {"name": "Suraj", "marks": 90}

file = open("data.dat", "wb")
pickle.dump(data, file)
file.close()

print("Object stored")