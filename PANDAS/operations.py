import pandas as pd

# Load data
df = pd.read_csv('study_tracker.csv')

# Explore
df.head() #first 5 rows
df.info() #Shows dataset structure, data types and missing values
df.describe() #Shows statistics such as mean, min, max and standard deviation

# Select columns
df['date'] #single column
df[['date', 'study_hours']] #multiple columns

# Filter rows
df[df['study_hours'] == 4.45] #Displays all rows in your DataFrame where study_hours is exactly 4.45
df[df['study_hours'] > 2.23] #displays all rows where study_hours is greater than 2.23 hours

# Sort
df.sort_values('study_hours', ascending=False) #sorts the dataset from highest to lowest
# ascending=True -> Ascending (default) ->	1, 2, 3, 4, 5
# ascending=False -> Descending	-> 5, 4, 3, 2, 1

#Group and aggregate
df.groupby('subject')['study_hours'].mean() #calculates the average number of study hours per session for each subject
# Step-by-step explanation:
# 1. df.groupby('subject') — groups all rows that have the same subject (Math, Database, Python, etc.).
# 2. ['study_hours'] — selects the study hours column.
# 3. .mean() — calculates the average study hours for each subject.
# Example
# Original dataset:
# subject	study_hours
# Database	2.0
# Math	3.0
# Database	4.0
# Python	1.5
# Math	2.0
# Python	2.5

# After running the code:
# subject	Average study_hours
# Database	3.0
# Math	2.5
# Python	2.0

df.groupby('subject')['study_hours'].sum() #calculates the total number of hours you spent studying each subject
# Step-by-step explanation:
# 1. df.groupby('subject') — groups rows by subject (Database, Math, Python, etc.).
# 2. ['study_hours'] — selects the study hours column.
# 3. .sum() — adds all study hours together for each subject.

# Example
# Original dataset:
# subject	study_hours
# Database	2.0
# Math	3.0
# Database	4.0
# Python	1.5
# Math	2.0
# Python	2.5

# After running the code:
# subject	Total study_hours
# Database	6.0
# Math	5.0
# Python	4.0

#Count values 
df['study_location'].value_counts() #counts how many study sessions you completed at each study location.
# Step-by-step explanation:
# 1. df['study_location'] — selects the study_location column.
# 2. .value_counts() — counts how many times each location appears.
# 3. Results are sorted from most frequent to least frequent.

# Example
# Original dataset:
# study_location
# Home
# Library
# Home
# Study Room
# Library
# Home

# Output:
# study_location
# Home          3
# Library       2
# Study Room    1

# This means you studied:
# - At Home — 3 sessions
# - At Library — 2 sessions
# - In Study Room — 1 session

# Handle missing data
df.dropna() #removes rows or columns containing missing values.
df.fillna(0) #replaces missing values with something else. in our case fill missing values by 0.
