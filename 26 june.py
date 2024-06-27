import pandas as pd

# From a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# From a CSV file
df = pd.read_csv('data.csv')
# Display the first 5 rows
print(df.head())

# Display the last 5 rows
print(df.tail())

# Display the shape of the DataFrame
print(df.shape)
# Access a column
print(df['Name'])

# Access a row by index
print(df.iloc[0])

# Access a specific cell
print(df.loc[0, 'Age'])
# Add a new column
df['Gender'] = ['Female', 'Male', 'Male']

# Drop a column
df = df.drop('City', axis=1)

# Sort the DataFrame
df = df.sort_values(by='Age', ascending=False)
# Check for missing values
print(df.isnull().sum())

# Fill missing values
df = df.fillna(0)
# Group by a column and calculate the mean
print(df.groupby('Gender')['Age'].mean())

# Apply a custom function to a column
df['Age_Squared'] = df['Age'].apply(lambda x: x**2)
# Create a DataFrame with a datetime index
df = pd.DataFrame({'Date': pd.date_range('2023-01-01', periods=10),
                   'Value': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]})
df = df.set_index('Date')

# Access data by datetime index
print(df.loc['2023-01-05'])

# Resample data by month
monthly_data = df.resample('M').mean()

# Create two DataFrames
df1 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                    'Age': [25, 30, 35]})
df2 = pd.DataFrame({'Name': ['Alice', 'Bob', 'David'],
                    'City': ['New York', 'London', 'Paris']})

# Merge the DataFrames on the 'Name' column
merged_df = pd.merge(df1, df2, on='Name', how='outer')