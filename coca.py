import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Suraj", 18, 85])
    writer.writerow(["Aman", 19, 90])

print("CSV file created")