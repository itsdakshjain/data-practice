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

# Create a distribution plot for Total Scores
plt.figure(figsize=(10, 6))
sns.histplot(df['total_score'], kde=True, color='skyblue')
plt.title('Distribution of Student Total Scores')
plt.xlabel('Total Score')
plt.ylabel('Frequency')

# Compare performance across different engineering branches
plt.figure(figsize=(12, 6))
sns.boxplot(x='branch', y='average_score', data=df, palette='Set2')
plt.title('Performance Comparison by Branch')
plt.xticks(rotation=45)
plt.tight_layout()

# Check correlation between Math and Science scores
plt.figure(figsize=(8, 6))
correlation = df[['math_score', 'science_score']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Score Correlation Heatmap')

# Export the plot to an image file for the report
plt.savefig('performance_analysis.png')
print("Visualization complete. Plot saved as 'performance_analysis.png'.")
