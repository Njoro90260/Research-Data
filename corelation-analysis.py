import pandas as pd
from scipy.stats import spearmanr

# Sample data (replace with your actual data)
data = {
    'Salting_Techniques': [4, 3, 5, 4, 3, 4, 5, 4, 4, 5, 3, 4, 5, 4, 4, 3, 5, 4, 4, 5, 4, 3, 4, 5, 4, 3, 5, 4, 4, 5],
    'Integration_Practices': [5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 4, 4, 5, 4, 5, 3, 5, 4, 3, 4, 5, 3, 4, 4, 5, 3, 4, 4, 5, 4],
    'Bcrypt_Effectiveness': [3, 4, 5, 4, 4, 5, 4, 4, 3, 5, 4, 4, 5, 3, 5, 4, 4, 3, 4, 4, 5, 3, 4, 5, 4, 3, 5, 4, 5, 4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate Spearman correlation
correlation_matrix = df.corr(method='spearman')

print("Spearman Correlation Matrix:")
print(correlation_matrix)

# Alternatively, you can calculate pairwise correlations:
spearman_corr, _ = spearmanr(df['Salting_Techniques'], df['Integration_Practices'])
print(f"Spearman Correlation between Salting Techniques and Integration Practices: {spearman_corr:.2f}")

spearman_corr_bcrypt, _ = spearmanr(df['Salting_Techniques'], df['Bcrypt_Effectiveness'])
print(f"Spearman Correlation between Salting Techniques and Bcrypt Effectiveness: {spearman_corr_bcrypt:.2f}")
