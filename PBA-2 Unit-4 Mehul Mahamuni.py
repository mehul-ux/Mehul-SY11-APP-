import pandas as pd

# Read employee data
df = pd.read_csv("employee.csv")

# Display employee details
print("Employee Details:")
print(df[["Name", "Department", "Salary"]])

# Calculate average salary department-wise
print("\nAverage Salary by Department:")
print(df.groupby("Department")["Salary"].mean())
