import numpy as np

# Responses for each statement (hypothetical)
def response():
    salting_responses = {
    'Statement 1': [5, 4, 5, 5, 4, 5, 5, 4, 5, 5, 5, 5, 4, 5, 5, 5, 4, 4, 5, 5, 4, 5, 5, 5, 4, 4, 5, 5, 5, 5, 4, 5, 4, 4, 5, 5, 5, 4, 5, 5, 4, 5],
    'Statement 2': [5, 4, 5, 5, 4, 5, 5, 4, 5, 4, 4, 5, 5, 4, 5, 5, 4, 5, 5, 5, 4, 5, 5, 4, 5, 5, 5, 5, 4, 4, 5, 5, 4, 5, 5, 5, 4, 4, 5, 4, 5, 5],
    'Statement 3': [5, 5, 4, 4, 5, 5, 4, 5, 5, 5, 5, 4, 4, 5, 5, 5, 4, 4, 5, 5, 5, 4, 5, 5, 4, 5, 5, 4, 5, 5, 5, 4, 5, 4, 5, 4, 5, 5, 4, 5, 5, 4],
    'Statement 4': [5, 4, 5, 4, 5, 5, 5, 4, 5, 5, 4, 5, 4, 5, 5, 5, 5, 4, 5, 4, 5, 5, 4, 5, 5, 5, 4, 5, 5, 4, 5, 4, 5, 5, 5, 4, 4, 5, 5, 4, 4, 5],
    'Statement 5': [5, 4, 4, 5, 5, 5, 4, 5, 4, 4, 5, 5, 4, 4, 5, 5, 5, 4, 4, 5, 4, 4, 5, 5, 5, 5, 4, 5, 4, 5, 5, 4, 5, 5, 4, 5, 5, 4, 5, 5, 5, 4],
    'Statement 6': [4, 5, 5, 5, 4, 5, 5, 4, 5, 4, 5, 4, 5, 4, 5, 5, 4, 5, 5, 4, 5, 5, 4, 5, 5, 4, 5, 4, 4, 5, 5, 4, 5, 5, 4, 5, 5, 4, 5, 4, 5, 5],
    'Statement 7': [5, 5, 4, 4, 5, 4, 5, 4, 5, 5, 4, 5, 5, 4, 5, 5, 5, 5, 4, 4, 5, 4, 4, 5, 5, 5, 4, 4, 5, 5, 5, 5, 4, 4, 5, 4, 4, 5, 5, 4, 4, 5],
    'Statement 8': [4, 4, 5, 4, 5, 5, 4, 4, 5, 4, 5, 5, 4, 5, 5, 4, 5, 5, 4, 5, 4, 5, 5, 4, 4, 5, 5, 5, 5, 4, 5, 4, 4, 5, 4, 5, 5, 5, 4, 4, 5, 5],
    'Statement 9': [5, 4, 5, 4, 5, 4, 5, 4, 5, 5, 4, 4, 4, 5, 5, 4, 5, 5, 4, 5, 4, 4, 5, 4, 5, 4, 4, 5, 5, 5, 4, 5, 4, 5, 5, 5, 4, 4, 4, 5, 4, 5],
    'Statement 10': [4, 5, 5, 4, 5, 4, 5, 5, 4, 5, 4, 5, 5, 4, 5, 4, 5, 5, 4, 4, 5, 5, 4, 5, 5, 4, 4, 5, 5, 4, 5, 5, 4, 5, 4, 4, 5, 5, 5, 4, 5, 4]
    }

    return salting_responses

r = response()    
# Calculate mean and standard deviation for each statement
results = {statement: (np.mean(data), np.std(data)) for statement, data in r.items()}
print(f"Salting Techniques Mean and Standard Deviations\n\n{results}\n\n")
# Calculate percentage for each unique response per statement
response_percentages = {}

for statement, data in r.items():
    unique, counts = np.unique(data, return_counts=True)
    percentages = {int(response): round((count / len(data)) * 100, 2) for response, count in zip(unique, counts)}
    response_percentages[statement] = percentages

for statement, responses in  response_percentages.items():
    print(f"Salting Techniques Percetages\n\n{statement}: Strongly Disagree (1): {responses.get(1, 0)}%, Disagree (2): {responses.get(2, 0)}%, Neutral (3): {responses.get(3, 0)}%, Agree (4): {responses.get(4, 0)}%, Strongly Agree (5): {responses.get(5, 0)}%")