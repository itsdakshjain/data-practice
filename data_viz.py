import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data from February
try:
    df = pd.read_csv('cleaned_student_data.csv')
    print("Visualizing data for", len(df), "students.")
    # Set visual style
    sns.set_theme(style="whitegrid")
except FileNotFoundError:
    print("Cleaned data not found. Please run the cleaner script first.")
