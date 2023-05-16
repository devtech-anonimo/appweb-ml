import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.inspection import permutation_importance
from sklearn.metrics import accuracy_score
import joblib

# Load data
dados_cardio = pd.read_csv('cardio_train.csv', sep=';')

# Rename columns
rename_columns = {
    'id': 'id',
    'age': 'age',
    'gender': 'gender',
    'height': 'height',
    'weight': 'weight',
    'ap_hi': 'systolic_pressure',
    'ap_lo': 'diastolic_pressure',
    'cholesterol': 'cholesterol',
    'gluc': 'glucose',
    'smoke': 'smoker',
    'alco': 'alcohol_intake',
    'active': 'physical_activity',
    'cardio': 'heart_disease'
}
dados_cardio.rename(columns=rename_columns, inplace=True)


# Split data into training and testing sets
dados_cardio.drop('id', axis=1, inplace=True)
X = dados_cardio.drop('heart_disease', axis=1)
y = dados_cardio['heart_disease']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a random forest classifier
ml_model = RandomForestClassifier(n_estimators=20, n_jobs=4, max_depth=4)
ml_model.fit(X_train, y_train)

# Make predictions on test set
predictions = ml_model.predict(X_test)

# Evaluate performance of the model
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

# Calculate feature importance
result = permutation_importance(ml_model, X_test, y_test, n_repeats=10, n_jobs=2)
importances = result.importances_mean
sorted_idx = importances.argsort()

# Print feature importance table
features = X.columns
table_data = [(f, round(importances[i], 4)) for i, f in enumerate(features[sorted_idx])]


# Save the model
joblib.dump(ml_model, './model/random_forest_cardio.pkl')

# Load the model
ml_model = joblib.load('./model/random_forest_cardio.pkl')

# Make predictions on test set
y_pred = ml_model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

print("Model accuracy: {:.2f}%".format(accuracy * 100))
