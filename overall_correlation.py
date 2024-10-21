import pandas as pd
from scipy.stats import spearmanr

# Load the data from CSV files
df = pd.read_csv('data/responses_data.csv')

# List the number of statements
num_statements = 10  # You have 10 statements in total

# Calculate pairwise correlations and their average
total_correlation = 0
for i in range(num_statements):
    spearman_corr, _ = spearmanr(df[f'Salting_Techniques_Statement_{i + 1}'], df[f'Integration_Practices_Statement_{i + 1}'])
    total_correlation += spearman_corr
    print(f"Spearman Correlation between Salting Techniques Statement {i + 1} and Integration Practices Statement {i + 1}: {spearman_corr:.2f}")

# Calculate the average correlation
average_correlation = total_correlation / num_statements
print(f"\nOverall Average Spearman Correlation: {average_correlation:.2f}")
