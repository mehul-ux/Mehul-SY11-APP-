import csv
import json

# Create and write data into CSV file
with open("input.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Rahul", "20", "CSE"])
    writer.writerow(["Amit", "21", "AI"])
    writer.writerow(["Priya", "20", "IT"])

# Read data from CSV file
with open("input.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)

# Convert CSV data to JSON and write to output file
with open("output.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data converted to JSON successfully.")
