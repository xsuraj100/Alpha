file = open("names.txt", "w")
names = input("Enter names separated by space: ")
file.write(names)
file.close()

file = open("names.txt", "r")
name_list = file.read().split()
name_list.sort()

print(name_list)
file.close()
