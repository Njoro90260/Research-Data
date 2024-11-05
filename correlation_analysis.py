import pandas as pd
from scipy.stats import spearmanr
from test import create_responses as create_test_responses
from test1 import create_responses as create_test1_responses

# Define the counts for each response category (Example dictionary, replace with actual counts)
test_counts = {5: 100, 4: 50, 3: 100, 2: 50, 1: 0}  # Example for test.py
test1_counts = {5: 0, 4: 50, 3: 100, 2: 50, 1: 100}  # Example for test1.py with slight variations

# Generate response lists
test_responses = create_test_responses(test_counts)
test1_responses = create_test1_responses(test1_counts)

# Check the length of the response lists
if len(test_responses) != len(test1_responses):
    print("Error: The lengths of the data lists are not equal. Please ensure all data has the same length.")
else:
    # Create a DataFrame using the extracted lists
    df = pd.DataFrame({
        'test_Responses': test_responses,
        'test1_Responses': test1_responses
    })

    # Save the DataFrame to a CSV file
    df.to_csv('data/responses_data.csv', index=False)  

    # Calculate Spearman correlation matrix
    correlation_matrix = df.corr(method='spearman')

    # Save the correlation matrix to another CSV file
    correlation_matrix.to_csv('data/correlation_matrix.csv')

    # Print the DataFrame and correlation matrix for verification
    print("Responses DataFrame saved to 'responses_data.csv':")
    print(df)
    print("\nSpearman Correlation Matrix saved to 'correlation_matrix.csv':")
    print(correlation_matrix)

    # Calculate pairwise correlations for each statement
    spearman_corr, _ = spearmanr(df['test_Responses'], df['test1_Responses'])
    print(f"Spearman Correlation between test responses and test1 responses: {spearman_corr:.2f}")
