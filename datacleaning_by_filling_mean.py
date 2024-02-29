import pandas as pd

data = pd.read_csv('/Users/utsuktakhatri/Desktop/data mining/employees.csv')
print("Original Data")
print(data[0:30])

# Method 1: Filling missing values with mean 
data['Salary']=data['Salary'].fillna(data['Salary'].mean())
print("Cleaned Data using Mean")
print(data[0:30])

data = pd.read_csv('/Users/utsuktakhatri/Desktop/data mining/employees.csv')
print("Original Data")
print(data[0:30])

# Method 2: Filling missing values with Linear interpolation
data['Salary']=data['Salary'].interpolate(method="linear")
print("Cleaned Data using linear interpolation")
print(data[0:30])