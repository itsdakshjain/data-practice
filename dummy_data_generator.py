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
