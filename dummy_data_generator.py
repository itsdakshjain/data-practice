import pandas as pd
import numpy as np

# Create a large dataset of 2000 students
rows = 2000
df = pd.DataFrame({
    'student_id': range(1001, 1001 + rows),
    'math_score': np.random.randint(30, 100, size=rows),
    'science_score': np.random.randint(30, 100, size=rows)
})
df['branch'] = np.random.choice(['CS', 'IT', 'ECE', 'ME'], size=rows)

# Intentionally creating missing data for later cleaning practice
for col in ['math_score', 'science_score']:
    df.loc[df.sample(frac=0.15).index, col] = np.nan

# INTRODUCE OUTLIERS & ANOMALIES
# Inject a few impossible negative scores and typo-based high scores
df.loc[df.sample(n=10).index, 'math_score'] = -50
df.loc[df.sample(n=10).index, 'science_score'] = 999
print("Data Generation Anomaly: Successfully injected out-of-bounds outliers for testing.")


df.to_csv('raw_data.csv', index=False)
print('Dataset Created Successfully')

# NEW FEATURE: DATA GENERATION SUMMARY LOGGING
print("\n=== RAW DATA GENERATION SUMMARY ===")
print(f"Total Student Records Generated: {len(df)}")
print("\nMissing Values Injected Per Column:")
print(df.isnull().sum()[['math_score', 'science_score']])
print("\nStudent Distribution by Branch:")
print(df['branch'].value_counts())
print("===================================")
# ----------------------------------------------------
