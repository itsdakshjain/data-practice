Data Practice: End-to-End Student Analytics

This project demonstrates a full data science workflow, from raw data generation to final visualization.

Project Structure

* **Data Generation:** Developed dummy_data_generator.py to create a 2000-row messy dataset.
* **Processing:** Built data_cleaning.py to handle missing values (imputation), filter outliers, add an automated student grading system, and run automated pipeline validation checks.
* **Visualization:** Created data_viz.py for statistical plotting, branch-wise performance analysis, and letter grade distribution tracking.
* **Documentation:** Finalized environment requirements and usage instructions.

How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Generate data: `python dummy_data_generator.py`
3. Clean data & validate pipeline: `python data_cleaning.py`
4. View results: `python data_viz.py`

Results

The project generates a comprehensive final analysis image containing core performance metrics: performance_analysis.png.
