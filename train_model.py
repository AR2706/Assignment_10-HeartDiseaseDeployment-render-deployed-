import kagglehub
import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Download latest version of the dataset
print("Downloading dataset...")
path = kagglehub.dataset_download("johnsmith88/heart-disease-dataset")
print("Path to dataset files:", path)

# Task 1: Data Understanding and Preprocessing
# Load the dataset using Pandas
csv_file_path = os.path.join(path, "heart.csv") # Assuming standard Kaggle filename
df = pd.read_csv(csv_file_path)

# Display the first five records
print("\n--- First 5 Records ---")
print(df.head())

# Identify target variable and numerical features (Assuming 'target' is the label column)
target_col = 'target' 
numerical_features = df.select_dtypes(include=['int64', 'float64']).columns.drop(target_col, errors='ignore').tolist()

print(f"\nTarget Variable: {target_col}")
print(f"Numerical Features: {numerical_features}")

# Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Drop rows with missing values (if any exist) or handle them
df = df.dropna()

# Split the dataset into 80% training and 20% testing
X = df.drop(columns=[target_col])
y = df[target_col]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Task 2: Model Development
print("\nTraining the Random Forest model...")
model = RandomForestClassifier(random_state=42, n_estimators=100)
model.fit(X_train, y_train)

# Evaluate using Accuracy Score
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy Score: {accuracy:.4f}")

# Save the trained model using Joblib
joblib.dump(model, 'model.pkl')
print("\nModel saved successfully as 'model.pkl'")