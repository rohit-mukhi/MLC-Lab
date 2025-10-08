import numpy as np
import pandas as pd

details = pd.DataFrame({
    'Name': ['Issei', 'Rias', 'Akeno', 'Asia', 'Xenovia', 'Kiba'],
    'Age': [21, 22, 19, 17, 18, 20],
    'Marks': [93, 88, 85, 82, 87, 86]
}, index=[1, 2, 3, 4, 5, 6])

print("Students details:")
print(details, "\n")
average_marks = np.mean(details['Marks'])
print(f"Average marks: {average_marks:.2f}\n")

criteria = details[(details['Age'] < 20) & (details['Marks'] > 60)]
print("Students who secured above 60 and are younger than 20 years are: ")
print(criteria)
