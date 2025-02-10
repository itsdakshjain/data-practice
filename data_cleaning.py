import pandas as pd
import numpy as np

# Load the messy data generated in January
try:
df = pd.read_csv('raw_data.csv')
print("Successfully loaded dataset for cleaning.")
except FileNotFoundError:
print("Raw data not found. Please run the generator first.")
