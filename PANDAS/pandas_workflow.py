import pandas as pd
import matplotlib.pyplot as plt

# 1) Load data
df = pd.read_csv('study_tracker.csv')

# 2) Filter - session longer than 2 hours
subset = df[df['study_hours'] > 2]

# 3) Group - total hours per subject
# summary = subset.groupby('subject')['study_hours'].sum()

summary = df.groupby('subject')['study_hours'].sum() #show all subjects

# 4) Visualize - bar chart
#horizontal bar chart:
summary.sort_values().plot(kind='barh')

plt.title('Total Study Hours by Subject')
plt.xlabel('Total Study Hours')
plt.ylabel('Subject')
plt.tight_layout()
plt.show()

# summary.plot(kind='bar')
# plt.xlabel('Subject')
# plt.ylabel('Total Study Hours')
# plt.title('Study Hours by Subject') #Adds a chart title
# plt.tight_layout() #Automatically adjusts the spacing in your chart so that labels, titles, and other elements don't overlap or get cut off.
# plt.show() #Display the chart
