import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class MinMaxNormalization:
    def minmax_scalar(self, d):
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(d)
        scaled_df = pd.DataFrame(scaled_data, columns=d.columns)
        return scaled_df

# Example usage
data = pd.DataFrame([[20000, 30], [25000, 32], [30000, 35], [37000, 37]], columns=['Salary', 'Age'])

print("\nOriginal Data:")
print(data)

minmax_scaler = MinMaxNormalization()
scaled_data = minmax_scaler.minmax_scalar(data)

print("\nMin-Max Scaled Data:")
print(scaled_data)
