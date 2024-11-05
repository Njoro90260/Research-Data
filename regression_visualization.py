import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data from CSV files
df = pd.read_csv('data/responses_data.csv') 

# Prepare the data for regression
test = df[f'test_Responses'].values
test1 =  df[f'test1_Responses'].values

# Flatten the arrays for regression
X = test.flatten().reshape(-1, 1)  
y = test1.flatten()  # Target (Integration Practices)

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
plt.xlabel('Average Response for test')
plt.ylabel('Average Response for test1')
plt.title('Linear Regression: test vs test1')

# Adding legend
plt.legend()

# Show the plot
plt.show()
