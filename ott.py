file = open("employee.txt", "a")

name = input("Name: ")
eid = input("Employee ID: ")
salary = input("Salary: ")

file.write(name + "," + eid + "," + salary + "\n")
file.close()

file = open("employee.txt", "r")
print(file.read())
file.close()
