file = open("data.txt", "r")
content = file.read()
file.close()

new_line = input("Enter new line: ")

file = open("data.txt", "w")
file.write(new_line + "\n" + content)
file.close()
