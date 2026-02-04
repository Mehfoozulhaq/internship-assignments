# House Price Prediction using Linear Regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the data (from Kaggle)
script_dir = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(os.path.join(script_dir, "house_prices_practice.csv"))

print("Dataset Overview:")
print(data.head())
print(f"\nDataset shape: {data.shape}")
print(f"\nColumn info:\n{data.info()}")

# Preprocessing
print("\nPreprocessing data...")
data = data.dropna()
data = pd.get_dummies(data, drop_first=True)

# Separate features and target
X = data.drop("SalePrice", axis=1)
y = data["SalePrice"]

print(f"Features: {list(X.columns)}")
print(f"Target: SalePrice")

# Split into train/test (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")

# Train the linear regression model
print("\nTraining model...")
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n=== Model Performance ===")
print(f"MAE (Mean Absolute Error): ${mae:,.2f}")
print(f"MSE (Mean Squared Error): ${mse:,.0f}")
print(f"RMSE (Root Mean Squared Error): ${rmse:,.2f}")
print(f"R² Score: {r2:.4f}")

# Show top features by coefficient magnitude
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
}).sort_values('Coefficient', key=abs, ascending=False)

print("\n=== Top 10 Important Features ===")
print(feature_importance.head(10))

# Visualization 1: Actual vs Predicted
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.xlabel("Actual Price ($)")
plt.ylabel("Predicted Price ($)")
plt.title("Actual vs Predicted House Prices")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Perfect Prediction')
plt.legend()
plt.tight_layout()
plt.show()

# Visualization 2: Residuals
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.6)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel("Predicted Price ($)")
plt.ylabel("Residuals ($)")
plt.title("Residual Plot")
plt.tight_layout()
plt.show()
