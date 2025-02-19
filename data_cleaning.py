import pandas as pd
import numpy as np

# Load the messy data generated in January
try:
df = pd.read_csv('raw_data.csv')
print("Successfully loaded dataset for cleaning.")
except FileNotFoundError:
print("Raw data not found. Please run the generator first.")

# Phase 1: Data Inspection
print("\n--- Basic Info ---")
print(df.info())
print("\n--- Missing Value Count ---")
print(df.isnull().sum())
print("\n--- Statistical Summary ---")
print(df.describe())

# Phase 2: Handling Missing Values
# We will fill scores based on the mean of their specific branch for better accuracy
df['math_score'] = df['math_score'].fillna(df.groupby('branch')['math_score'].transform('mean'))
df['science_score'] = df['science_score'].fillna(df.groupby('branch')['science_score'].transform('mean'))

# Remove students with impossible scores (below 0 or above 100)
df = df[(df['math_score'] >= 0) & (df['math_score'] <= 100)]
df = df[(df['science_score'] >= 0) & (df['science_score'] <= 100)]
print("Data cleaning: Nulls handled and outliers removed.")
