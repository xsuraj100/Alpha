file = open("data.txt", "r")
text = file.read()
file.close()

new_text = ""

for ch in text:
    if not ch.isdigit():
        new_text += ch

file = open("data.txt", "w")
file.write(new_text)
file.close()

print("Digits removed")