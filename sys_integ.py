import numpy as np

# Responses for the new set of 10 statements based on the system integration objective

def response_integration():
    integration_responses = {
    1: [4] * 32 + [3] * 4 + [2] * 6,
    2: [5] * 30 + [4] * 8 + [3] * 4,
    3: [4] * 28 + [3] * 10 + [2] * 4,
    4: [5] * 30 + [4] * 8 + [3] * 4,
    5: [4] * 28 + [3] * 10 + [2] * 4,
    6: [4] * 32 + [3] * 4 + [2] * 6,
    7: [5] * 30 + [4] * 8 + [3] * 4,
    8: [4] * 28 + [3] * 10 + [2] * 4,
    9: [5] * 30 + [4] * 8 + [3] * 4,
    10: [5] * 30 + [4] * 8 + [3] * 4,
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
