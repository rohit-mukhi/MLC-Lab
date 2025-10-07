import pandas as pd

report_card = {
    'Name': ['Tintin', 'Haddock', 'Mitsuhirato', 'Alcazar', 'Pablo'],
    'English': [98, 78, 65, 82, 75],
    'Mathematics': [100, 93, 82, 87, 76],
    'Science': [94, 86, 74, 68, 59]
}

df = pd.DataFrame(report_card)

df['Total'] = df[['English', 'Mathematics', 'Science']].sum(axis=1)
df['Average'] = df['Total']/3

topper = df.loc[df['Average'].idxmax()]

print("Student marks dataframe:\n", df)
print(f"\nTopper: {topper['Name']} with average of {topper['Average']:.2f}")
