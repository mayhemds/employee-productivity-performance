# Employee Productivity & Performance Dashboard

## 📌 Project Overview

This project analyzes employee work habits and predicts performance scores. The dataset contains various employee attributes, including work hours, sick days, and performance scores. The goal is to clean the data, extract meaningful insights, and visualize key trends to improve workforce efficiency.

## 📂 Dataset

- **File:** `employee_performance.xlsx`
- **Columns Include:**
  - Employee ID
  - Department
  - Work Hours
  - Sick Days
  - Projects Completed
  - Performance Score
  - Other relevant metrics

## 🎯 Objectives

- **Data Cleaning:**
  - Fill missing performance scores using the mean value.
  - Categorize employees based on work hours (e.g., Low, Medium, High, Very High).
  - Remove duplicate entries and outliers.
- **Data Analysis:**
  - Correlation analysis between sick days and performance scores.
  - Identify overworked employees (high work hours, low performance).
- **Data Visualization:**
  - **Bar Chart:** Departments with the highest productivity.
  - **Scatter Plot:** Work hours vs. performance scores.
  - **Heatmap:** Correlation between sick days, projects completed, and performance.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Libraries:**
  - `pandas` (Data Processing)
  - `numpy` (Numerical Computations)
  - `matplotlib` & `seaborn` (Data Visualization)
  - `openpyxl` (Excel File Handling)

## 🚀 How to Run This Project

```sh
# Clone the repository
git clone https://github.com/mayhemds/employee-performance-dashboard.git
cd employee-performance-dashboard

# Install dependencies
pip install pandas numpy matplotlib seaborn openpyxl

# Run the Python script
python employee_performance_analysis.py

## 📈 Results & Insights

- Employees with high sick days tend to have lower performance scores.
- Overworked employees show a decline in productivity.
- Certain departments have significantly higher productivity than others.

## 🔗 Project Links

- **Live Dashboard (if applicable):** [[Link to Live Dashboard](https://employee-appuctivity-performance-l97jywvpomphn9vxu3fqze.streamlit.app/)]

## 📬 Contact

For any questions or contributions, feel free to reach out:

_This project is part of my portfolio to demonstrate my skills in data analysis and visualization._ 🚀
