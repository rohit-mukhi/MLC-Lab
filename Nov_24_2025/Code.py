import pandas as pd

room_length = [20,30,15,12, 22,10]
room_breadth = [20,20,10,11,19,14]
room_type =["big","big","normal","normal", "big","normal"]

data = pd.DataFrame({
    'Length': room_length,
    'Breadth': room_breadth,
    'Type': room_type
})
**************************************************************************************************************
print(data)

age = [10,13,20,19,18,22,21]
city = ["City A","City B","City B", "City A","City A","City C", "City B"]

data = pd.DataFrame({
    'age': age,
    'city': city,
})

print(data)

*****************************************************************************************************************
# This is how to create dummy features
dummy_features = pd.get_dummies(data['city'])
data_age = pd.DataFrame(data=data, columns=['age'])
data_mod = pd.concat([data_age.reset_index(drop=True), dummy_features], axis=1)
print(data_mod)

******************************************************************************************************************

import pandas as pd
from sklearn import preprocessing

marks_science = [78,56,87,91,45,62]
marks_maths = [75,62,90,95,42,57]
grade = ['B','C', 'A', 'A','D','B']

data = pd.DataFrame({
    'Science Marks': marks_science,
    'Maths Marks': marks_maths,
    'Total Grade': grade
})

print(data)

*********************************************************************************************************************

