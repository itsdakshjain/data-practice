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

# Phase 3: Feature Engineering
df['total_score'] = df['math_score'] + df['science_score']
df['average_score'] = df['total_score'] / 2

# --- AUTOMATED STUDENT GRADING ---
def assign_grade(score):
    """Maps an average score to a letter grade."""
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

# Apply grading logic based on the calculated average_score
df['final_grade'] = df['average_score'].apply(assign_grade)
print("Feature Engineering: Successfully added 'final_grade' column.")


# --- NEW FEATURE: Data Quality Pipeline Validation  ---
print("\n--- Running Final Data Quality Checks ---")
null_check = df.isnull().sum().sum()
outlier_check = df[(df['math_score'] < 0) | (df['math_score'] > 100) | (df['science_score'] < 0) | (df['science_score'] > 100)].shape[0]

if null_check == 0 and outlier_check == 0:
    print("✓ PASS: Zero missing values found in final dataset.")
    print("✓ PASS: All scores are within valid 0-100 limits.")
    print(f"✓ PASS: Total clean student records ready for analysis: {df.shape[0]}")
else:
    print("⚠ WARNING: Data validation failed. Please check data processing steps.")

# Saving the final cleaned version
df.to_csv('cleaned_student_data.csv', index=False)
print("\nSUCCESS: Cleaned data saved to 'cleaned_student_data.csv'")


