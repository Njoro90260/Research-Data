import pandas as pd
from scipy import stats

# Load your data (replace 'your_data.csv' with the path to your data file)
# Ensure that your data has columns corresponding to different groups.
df = pd.read_csv('data/responses_data.csv')

# For example, let's say you have three groups: Group1, Group2, Group3
group1 = df['Group1'].dropna()
group2 = df['Group2'].dropna()
group3 = df['Group3'].dropna()
group4 = df['Group4'].dropna()
group5 = df['Group5'].dropna()
group6 = df['Group6'].dropna()
group7 = df['Group7'].dropna()
group8 = df['Group8'].dropna()
group9 = df['Group9'].dropna()
group10 = df['Group10'].dropna()
group11 = df['Group11'].dropna()
group12 = df['Group12'].dropna()
group13 = df['Group13'].dropna()
group14 = df['Group14'].dropna()
group15 = df['Group15'].dropna()
group16 = df['Group16'].dropna()
group17 = df['Group17'].dropna()
group18 = df['Group18'].dropna()
group19 = df['Group19'].dropna()
group20 = df['Group20'].dropna()


# Perform ANOVA
f_statistic, p_value = stats.f_oneway(group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12, group13, group14, group15, group16, group17, group18, group19, group20)

# Display the results
print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There are significant differences between groups.")
else:
    print("Fail to reject the null hypothesis: No significant differences between groups.")
