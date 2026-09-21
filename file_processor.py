# File Processing Program
# Count lines, extract first two lines, and write them to another file


def count_lines(filename):
    with open(filename, "r") as file:
        return sum(1 for line in file)


def extract_first_two_lines(filename):
    with open(filename, "r") as file:
        return [file.readline(), file.readline()]


def write_lines(filename, lines):
    with open(filename, "w") as file:
        file.writelines(lines)


# Main program
input_file = "input.txt"
output_file = "output.txt"

# Create input file
with open(input_file, "w") as file:
    file.write("Monday: Team meeting\n")
    file.write("Tuesday: Client review\n")
    file.write("Wednesday: Code review\n")
    file.write("Thursday: Project planning\n")
    file.write("Friday: Deployment\n")


# Count total lines
total = count_lines(input_file)
print("Total number of lines:", total)


# Extract first two lines
first_two = extract_first_two_lines(input_file)

print("\nFirst two lines:")
for line in first_two:
    print(line.strip())


# Write first two lines into output file
write_lines(output_file, first_two)

print("\nFirst two lines have been written to", output_file)


# Display output file
print("\nContents of output.txt:")

with open(output_file, "r") as file:
    print(file.read())