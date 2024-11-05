import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data from CSV files
df = pd.read_csv('data/responses_data.csv')

# Prepare the data for regression with the correct column names
X = df['test_Responses'].values.reshape(-1, 1)  # Independent variable
y = df['test1_Responses'].values  # Dependent variable

# Create and fit the Linear Regression model
reg_model = LinearRegression()
reg_model.fit(X, y)

# Get the regression coefficient (slope) and intercept
slope = reg_model.coef_[0]
intercept = reg_model.intercept_

# Predict the values based on the model
y_pred = reg_model.predict(X)

# Print the regression results
print(f"Linear Regression Equation: y = {slope:.2f} * x + {intercept:.2f}")

# Optional: Calculate R-squared value
r_squared = reg_model.score(X, y)
print(f"R-squared: {r_squared:.2f}")

# Optional: Show the predicted vs actual values for a quick comparison
df_results = pd.DataFrame({'Actual': y, 'Predicted': y_pred})
print("\nActual vs Predicted:")
print(df_results.head())
