import pandas as pd
from scipy.stats import spearmanr
from salting_tq import response  # Assuming response() returns a dictionary
from sys_integ import response_integration  # Assuming response_integration() returns a dictionary

# Get the response data
salting_responses = response()  # Call the function to get salting data
integration_responses = response_integration()  # Call the function to get integration data

# Extract the response lists for all statements
salting_techniques = [salting_responses[key] for key in salting_responses.keys()]
integration_practices = [integration_responses[key] for key in integration_responses.keys()]

# Check the length of the response lists
num_statements = len(salting_techniques)
if num_statements != len(integration_practices):
    print("Error: The lengths of the data lists are not equal. Please ensure all data has the same length.")
else:
    # Create a DataFrame using the extracted lists
    data = {}
    for i in range(num_statements):
        data[f'Salting_Techniques_Statement_{i + 1}'] = salting_techniques[i]
        data[f'Integration_Practices_Statement_{i + 1}'] = integration_practices[i]

    df = pd.DataFrame(data)

    # Print the DataFrame for verification
    print("DataFrame:")
    print(df)

    # Calculate Spearman correlation matrix
    correlation_matrix = df.corr(method='spearman')

    print("Spearman Correlation Matrix:")
    print(correlation_matrix)

    # Calculate pairwise correlations for each statement
    for i in range(num_statements):
        spearman_corr, _ = spearmanr(df[f'Salting_Techniques_Statement_{i + 1}'], df[f'Integration_Practices_Statement_{i + 1}'])
        print(f"Spearman Correlation between Salting Techniques Statement {i + 1} and Integration Practices Statement {i + 1}: {spearman_corr:.2f}")
