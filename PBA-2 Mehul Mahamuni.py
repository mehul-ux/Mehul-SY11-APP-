import os

# Get the folder where read.py is saved
folder = os.path.dirname(os.path.abspath(__file__))

source_path = os.path.join(folder, "source.txt")
destination_path = os.path.join(folder, "destination.txt")

with open(source_path, "r") as source:
    content = source.read()

with open(destination_path, "w") as destination:
    destination.write(content)

print("File contents copied successfully!")
