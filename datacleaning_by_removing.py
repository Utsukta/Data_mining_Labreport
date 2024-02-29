import pandas as pd

data = pd.read_csv('/Users/utsuktakhatri/Desktop/data mining/employees.csv')
print("Original Data")
print(data[0:30])

# Removing missing values
data=data.dropna(axis=0)

# Removing duplicate rows
data.drop_duplicates(keep='first',inplace=True)

# Removing column Boonus %
del data['Bonus %']

# Correcting Inconsitencies among values
data['Team']=data['Team'].str.replace('Fin','Finance')
data['Team']=data['Team'].str.replace('Mkt','Marketing')
data['Team']=data['Team'].str.replace('Financeance','Finance')

print("Cleaned Data is")
print(data[0:30])
data.to_csv('/Users/utsuktakhatri/Desktop/data mining/employees_cleaned.csv', index=False)
print("Data Successfully Cleaned")