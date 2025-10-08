import pandas as pd
import numpy as np

data = {
    'A': [10, 20, np.nan, 40, 50, np.nan, 70],
    'B': [100, np.nan, 300, 400, 500, 600, 700],
    'C': [1.1, 2.2, 3.3, np.nan, np.nan, 6.6, np.nan]
}
df = pd.DataFrame(data)

print("--- Initial DataFrame (a) ---")
print(df)
print(f"\nTotal missing values before cleaning: {df.isna().sum().sum()}")

column_means = df.mean()

df_filled = df.fillna(column_means)

print("\n--- DataFrame after Filling NaNs with Column Mean (b) ---")
print(df_filled)

df_dropped = df_filled.dropna(thresh=df_filled.shape[1] - 1)

print("\n--- Rows Dropped from ORIGINAL DataFrame (a) based on thresh=2 (c) ---")

df_final = df.dropna(thresh=df.shape[1] - 1)

print(df_final)
print(f"\nTotal rows kept: {len(df_final)} (Dropped rows had > 1 NaN)")
