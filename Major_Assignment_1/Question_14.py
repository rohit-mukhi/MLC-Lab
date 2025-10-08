import numpy as np
import pandas as pd

report = pd.DataFrame({
    'Name': ['Harry', 'Ron', 'Hermione', 'Tom', 'Snape'],
    'Tasks_Completed': [7, 5, 6, 10, 18],
    'Hours_Worked': [5, 3, 6, 9, 10]
}, index=[1, 2, 3, 4, 5])

report['Efficiency'] = (report['Tasks_Completed']/report['Hours_Worked'])

highest_efficiency = report['Efficiency'].idxmax()
highest_performer = report.loc[highest_efficiency]

print("Work Report: ")
print(report, "\n")
print("Highest performer:")
print(highest_performer)
