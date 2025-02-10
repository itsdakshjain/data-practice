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
