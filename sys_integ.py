import numpy as np

# Responses for the new set of 10 statements based on the system integration objective

def response_integration():
    integration_responses = {
    "Statement 1": [4, 5, 3, 4, 5, 5, 3, 4, 4, 5, 4, 3, 5, 4, 5, 3, 4, 5, 5, 3, 4, 4, 5, 4, 5, 3, 4, 4, 5, 5, 3, 4, 4, 5, 4, 3, 5, 4, 5, 4, 5, 4],
    "Statement 2": [3, 4, 3, 4, 5, 5, 4, 3, 4, 5, 4, 4, 5, 4, 4, 3, 4, 5, 4, 3, 4, 4, 5, 4, 5, 3, 3, 4, 5, 4, 4, 3, 4, 5, 4, 3, 5, 4, 4, 3, 4, 5],
    "Statement 3": [5, 4, 4, 5, 5, 4, 3, 4, 5, 4, 3, 5, 4, 5, 4, 3, 5, 4, 5, 4, 3, 4, 5, 4, 4, 3, 4, 4, 5, 5, 4, 3, 4, 5, 4, 4, 4, 5, 3, 4, 4, 5],
    "Statement 4": [4, 5, 4, 4, 5, 5, 4, 3, 4, 5, 3, 4, 4, 5, 4, 3, 5, 4, 4, 5, 3, 4, 4, 4, 5, 4, 4, 4, 4, 5, 3, 4, 4, 5, 4, 3, 5, 4, 4, 4, 5, 4],
    "Statement 5": [3, 4, 4, 4, 5, 4, 4, 3, 5, 4, 3, 4, 4, 5, 4, 4, 4, 4, 5, 3, 3, 4, 4, 4, 5, 4, 4, 4, 4, 5, 4, 3, 4, 4, 4, 3, 5, 4, 4, 4, 5, 3],
    "Statement 6": [4, 5, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 4, 5, 4, 4, 5, 4, 5, 3, 4, 4, 5, 4, 4, 3, 4, 4, 5, 4, 3, 4, 4, 5, 4, 3, 4, 4, 5, 4, 5, 3],
    "Statement 7": [3, 4, 4, 4, 5, 5, 3, 4, 4, 5, 3, 4, 4, 5, 4, 3, 4, 4, 5, 4, 3, 4, 4, 5, 5, 4, 3, 4, 4, 5, 4, 4, 4, 5, 4, 3, 5, 4, 5, 4, 4, 4],
    "Statement 8": [4, 5, 3, 4, 5, 5, 3, 4, 4, 5, 3, 4, 4, 5, 3, 4, 4, 4, 5, 3, 3, 4, 5, 4, 5, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 3, 5, 4, 4, 4, 5, 3],
    "Statement 9": [5, 4, 3, 4, 5, 4, 4, 3, 5, 4, 4, 4, 5, 4, 4, 3, 5, 4, 4, 4, 3, 4, 5, 4, 4, 4, 4, 4, 4, 5, 4, 3, 4, 5, 4, 3, 5, 4, 5, 4, 5, 4],
    "Statement 10": [3, 4, 4, 5, 4, 5, 3, 4, 5, 4, 4, 3, 5, 4, 4, 3, 5, 4, 5, 3, 3, 4, 4, 4, 5, 4, 4, 4, 5, 4, 3, 4, 4, 5, 4, 4, 5, 4, 4, 3, 5, 4]
    }
    return integration_responses
r = response_integration()
results = {statement: (np.mean(data), np.std(data)) for statement, data in r.items()}
print(f"Mean and Standard Deviation: \n\n{results}\n\n")

# Calculate percentage for each unique response per statement
response_percentages = {}

for statement, data in r.items():
    unique, counts = np.unique(data, return_counts=True)
    percentages = {int(response): round((count / len(data)) * 100, 2) for response, count in zip(unique, counts)}
    response_percentages[statement] = percentages

# Print response percentages
for statement, responses in response_percentages.items():
    print(f"System Integration Practices Percentages: \n\n{statement}: Strongly Disagree (1): {responses.get(1, 0)}%, Disagree (2): {responses.get(2, 0)}%, Neutral (3): {responses.get(3, 0)}%, Agree (4): {responses.get(4, 0)}%, Strongly Agree (5): {responses.get(5, 0)}%")
