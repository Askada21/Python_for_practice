import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('study_tracker.csv')

# One Line Code
df[df['study_hours'] > 2].groupby('subject')['productivity(1-5)'].mean().plot(kind='bar')

plt.title('Average Productivity by Subject')
plt.xlabel('Subject')
plt.ylabel('Average Productivity')
plt.tight_layout()
plt.show()