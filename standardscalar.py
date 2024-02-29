import pandas as pd
from sklearn.preprocessing import StandardScaler

# Create a sample DataFrame
data = pd.DataFrame({
    'Salary': [100000, 30000, 470000, 770000],
    'Age': [41, 35, 42, 37]
})

# Instantiate the StandardScaler
scaler = StandardScaler()

# Fit and transform the data using StandardScaler
scaled_data = scaler.fit_transform(data)

# Convert the scaled data back to a DataFrame for readability
scaled_df = pd.DataFrame(scaled_data, columns=data.columns)

# Display the original and scaled data
print("Original Data:")
print(data)
print("\nScaled Data:")
print(scaled_df)
