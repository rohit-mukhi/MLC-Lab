import pandas as pd

employee_sheet = {
    'ID': [101, 102, 103, 104],
    'Name': ['Elliot', 'Darlene', 'Trenton', 'Mobley'],
    'Salary': [200, 175, 120, 150]
}

df = pd.DataFrame(employee_sheet)

df['Bonus'] = df['Salary'] * 0.10

average_salary = df['Salary'].mean()
above_average = df[df['Salary'] > average_salary]

print("Employees details: \n", df)
print(f"\nAverage salary of employees: ${average_salary:.2f}K")
print("\nEmployees with salary above average: \n", above_average)
