import pandas as pd

df = pd.read_csv('study_tracker.csv')

#Display total number of study records
print(f"We have {len(df)} study records!") #Counts the total number of rows

#Display column names
print(f"Columns: {list(df.columns)}") #Displays all column names

#Display the first study record
print("\nFirst study session:")
print(df.iloc[0]) #Displays the first row (index 0)

# the study session with the highest number of study hours.
 
# Which study session was the longest?
longest_session = df.nlargest(1, 'study_hours') #Finds the row with the highest study hours
                #1 - Returns only one row | study_hours - Column used to find the largest value
print(longest_session[['date', 'subject', 'study_hours']]) #Displays only these three columns

smallest_ses = df.nsmallest(2, 'study_hours')
print(smallest_ses[['date', 'subject', 'study_hours']])
# nlargest() → finds the highest values.
# nsmallest() → finds the lowest values.