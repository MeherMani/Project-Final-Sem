import pandas as pd
import numpy as np

# Define the number of rows you want in your dataset
num_rows = 100

# Define the possible values for categorical columns
possible_education_levels = ['High School', "Bachelor's", "Master's", 'PhD']
possible_departments = ['Sales', 'HR', 'Research & Dev']
possible_genders = ['Male', 'Female']
possible_marital_statuses = ['Married', 'Single', 'Divorced']
possible_yes_no = ['Yes', 'No']

# Generate random data
data = {
    'Age': np.random.randint(18, 61, num_rows),
    'DistanceFromHome': np.random.randint(1, 36, num_rows),
    'Education': np.random.choice(possible_education_levels, num_rows),
    'EmployeeCount': np.ones(num_rows, dtype=int),
    'EmployeeID': np.arange(1, num_rows + 1),
    'JobLevel': np.random.randint(1, 6, num_rows),
    'MonthlyIncome': np.random.randint(10000, 200001, num_rows),
    'NumCompaniesWorked': np.random.randint(0, 10, num_rows),
    'PercentSalaryHike': np.random.randint(11, 26, num_rows),
    'StandardHours': np.ones(num_rows, dtype=int) * 8,
    'StockOptionLevel': np.random.randint(0, 4, num_rows),
    'TotalWorkingYears': np.random.randint(1, 26, num_rows),
    'TrainingTimesLastYear': np.random.randint(0, 7, num_rows),
    'YearsAtCompany': np.random.randint(0, 41, num_rows),
    'YearsSinceLastPromotion': np.random.randint(0, 16, num_rows),
    'YearsWithCurrManager': np.random.randint(0, 18, num_rows),
    'PerformanceRating': np.random.randint(1, 5, num_rows),
    'JobInvolvement': np.random.randint(1, 5, num_rows),
    'EnvironmentSatisfaction': np.random.randint(1, 5, num_rows),
    'JobSatisfaction': np.random.randint(1, 5, num_rows),
    'WorkLifeBalance': np.random.randint(1, 5, num_rows),
    'Department': np.random.choice(possible_departments, num_rows),
    'Gender': np.random.choice(possible_genders, num_rows),
    'MaritalStatus': np.random.choice(possible_marital_statuses, num_rows),
    'OverTime': np.random.choice(possible_yes_no, num_rows),
    'Attrition': np.random.choice(possible_yes_no, num_rows)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv('employee_dataset.csv', index=False)
