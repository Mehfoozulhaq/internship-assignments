# House Price Prediction Using Linear Regression

## Description
This assignment focuses on building a **Linear Regression model** to predict house prices based on various features such as number of rooms, size of the house, location, and other relevant factors.  
The objective is to understand the complete machine learning workflow, including data preprocessing, model training, and evaluation.
## Dataset
- The dataset was collected from **Kaggle**
- It contains information related to house features and their corresponding prices
- The dataset is stored as `housing.csv`
## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
## Steps Performed
1. Loaded the dataset using Pandas  
2. Handled missing values by removing incomplete records  
3. Converted categorical features (such as location) into numerical format using one-hot encoding  
4. Selected input features and target variable (house price)  
5. Split the dataset into training and testing sets  
6. Trained a Linear Regression model  
7. Evaluated the model using MAE, MSE, RMSE, and R² score  
8. Visualized actual vs predicted house prices  
## Model Used
**Linear Regression**  
A supervised machine learning algorithm used to predict continuous values by learning the relationship between input features and the target variable.
## Evaluation Metrics
 **Mean Absolute Error (MAE)**
 **Mean Squared Error (MSE)**
 **Root Mean Squared Error (RMSE)**
 **R² Score**
These metrics help measure the accuracy and performance of the model.
## Project Files
- `house_price_prediction.py` – Contains the complete implementation
- `house_price_practice.csv` – Dataset used for training and testing
- `README.md` – Project documentation
## Outcome
The model is able to predict house prices with reasonable accuracy based on the provided features, demonstrating the practical application of Linear Regression in real-world scenarios.
- **Your Name**
- Python Development Intern
