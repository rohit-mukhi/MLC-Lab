import pandas as pd

marks = [67, 34, 87, 56, 93, 21, 82, 38]

marksheet = pd.Series(marks, index=['1', '2', '3', '4', '5', '6', '7', '8'])
print("Original marksheet:")
print(marksheet, "\n")

new_marksheet = marksheet.copy()
new_marksheet[new_marksheet < 40] = "Fail"
print("New Marksheet:")
print(new_marksheet, "\n")

passed_count = (new_marksheet != "Fail").sum()
print(f"Number of students who passed: {passed_count}")

