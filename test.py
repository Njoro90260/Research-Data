import numpy as np

# Function to create responses based on specific counts
def create_responses(counts):
    # counts is a dictionary with keys as response categories and values as their counts
    return (
        [5] * counts.get(5, 0) +  # Strongly Agree
        [4] * counts.get(4, 0) +  # Agree
        [3] * counts.get(3, 0) +  # Neutral
        [2] * counts.get(2, 0) +  # Disagree
        [1] * counts.get(1, 0)     # Strongly Disagree
    )

# Function to calculate mean and standard deviation
def calculate_statistics(responses):
    results = {statement: (np.mean(data), np.std(data)) for statement, data in responses.items()}
    return results

# Function to calculate response percentages
def calculate_response_percentages(responses):
    response_percentages = {}
    for statement, data in responses.items():
        unique, counts = np.unique(data, return_counts=True)
        percentages = {int(response): round((count / len(data)) * 100, 2) for response, count in zip(unique, counts)}
        response_percentages[statement] = percentages
    return response_percentages

# Main execution
num_statements = 10  # Set the number of statements
# Define the specific counts for responses
counts = {
    5: 78,  # Strongly Agree
    4: 65,   # Agree
    3: 46,  # Neutral
    2: 12,   # Disagree
    1: 0     # Strongly Disagree (none in this case)
}

# Create responses for each statement
responses = {f"Statement {i}": create_responses(counts) for i in range(1, num_statements + 1)}

# Calculate statistics and print results
results = calculate_statistics(responses)
print(f"Mean and Standard Deviation: \n\n{results}\n\n")

# Calculate and print response percentages
response_percentages = calculate_response_percentages(responses)
print("Percentages:")
for statement, responses in response_percentages.items():
    print(f"\n\n{statement}: Strongly Disagree (1): {responses.get(1, 0)}%, Disagree (2): {responses.get(2, 0)}%, Neutral (3): {responses.get(3, 0)}%, Agree (4): {responses.get(4, 0)}%, Strongly Agree (5): {responses.get(5, 0)}%")
