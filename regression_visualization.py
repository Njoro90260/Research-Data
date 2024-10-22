import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data from CSV files
df = pd.read_csv('data/responses_data.csv') 

# Prepare the data for regression
salting_techniques = df[[f'Salting_Techniques_Statement_{i + 1}' for i in range(10)]].values
integration_practices = df[[f'Integration_Practices_Statement_{i + 1}' for i in range(10)]].values

# Flatten the arrays for regression
X = salting_techniques.flatten().reshape(-1, 1)  # Features (Salting Techniques)
y = integration_practices.flatten()  # Target (Integration Practices)

# Create and fit the Linear Regression model
reg_model = LinearRegression()
reg_model.fit(X, y)

# Predict the values based on the model
y_pred = reg_model.predict(X)

# Plot the data
plt.style.use('seaborn')
plt.scatter(X, y, color='blue', label='Actual data points', alpha=0.6)
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression line')

# Adding labels and title
plt.xlabel('Average Response for Salting Techniques')
plt.ylabel('Average Response for Integration Practices')
plt.title('Linear Regression: Salting Techniques vs Integration Practices')

# Adding legend
plt.legend()

# Show the plot
plt.show()
