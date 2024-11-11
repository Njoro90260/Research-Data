import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style("whitegrid")

# Load the data from CSV files
df = pd.read_csv('data/responses_data.csv')

# List the number of statements
num_statements = 10  # You have 10 statements in total

# Calculate pairwise correlations and store them
correlations = []
for i in range(num_statements):
    spearman_corr, _ = spearmanr(df[f'Salting_Techniques_Statement_{i + 1}'], df[f'Integration_Practices_Statement_{i + 1}'])
    correlations.append(spearman_corr)
    print(f"Spearman Correlation between Salting Techniques Statement {i + 1} and Integration Practices Statement {i + 1}: {spearman_corr:.2f}")

# Calculate the average correlation
average_correlation = sum(correlations) / num_statements
print(f"\nOverall Average Spearman Correlation: {average_correlation:.2f}")

# Plot the individual correlations for each statement pair
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_statements + 1), correlations, marker='o', color='skyblue', linestyle='-', linewidth=2, markersize=6)
plt.axhline(y=average_correlation, color='red', linestyle='--', label=f'Average Correlation: {average_correlation:.2f}')

# Add titles and labels
plt.title("Spearman Correlation per Statement Pair")
plt.xlabel("Statement Pair Number")
plt.ylabel("Spearman Correlation")
plt.xticks(range(1, num_statements + 1))
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()
