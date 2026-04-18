import csv

data = [
    {"Name": "A", "Marks": 80},
    {"Name": "B", "Marks": 90}
]

with open("data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Marks"])
    writer.writeheader()
    writer.writerows(data)