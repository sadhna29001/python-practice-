# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [10, 20, 30, 40, 50],
                   'C': [100, 200, 300, 400, 500]},
                  index=['a', 'b', 'c', 'd', 'e'])

# Access a column
print(df['A'])

# Access a row by label
print(df.loc['b'])

# Access a row by integer index
print(df.iloc[2])

# Slice a range of rows
print(df.loc['b':'d'])

# Slice a range of columns
print(df[['A', 'C']])

# Create a new column
df['D'] = df['A'] + df['B']

# Drop a column
df = df.drop('D', axis=1)

# Apply a function to a column
df['A_squared'] = df['A'].apply(lambda x: x**2)



# Replace values
df['B'] = df['B'].replace(20, 25)

# Melt the DataFrame (convert from wide to long format)
melted_df = pd.melt(df, id_vars=['A'], var_name='variable', value_name='value')

# Pivot the DataFrame (convert from long to wide format)
pivoted_df = melted_df.pivot(index='A', columns='variable', values='value')

# Create a multi-level DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6],
                   ('B', 'X'): [10, 20, 30, 40, 50, 60],
                   ('B', 'Y'): [100, 200, 300, 400, 500, 600]},
                  index=['a', 'b', 'c', 'd', 'e', 'f'])

# Stack the DataFrame (convert from wide to long format)
stacked_df = df.stack()

# Unstack the DataFrame (convert from long to wide format)
unstacked_df = stacked_df.unstack()


# Create a sample DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
                   'Age': [25, 30, 35, 27, 32],
                   'City': ['New York', 'London', 'Paris', 'New York', 'London']})

# Group by a single column and calculate the mean
print(df.groupby('City')['Age'].mean())

# Group by multiple columns and calculate multiple aggregations
print(df.groupby(['City', 'Name'])['Age'].agg(['min', 'max', 'mean']))

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [10, 20, 30, 40, 50]})

# Apply a function to each element of a DataFrame
df['A_squared'] = df['A'].apply(lambda x: x**2)

# Apply a function to each row of a DataFrame
df['A_plus_B'] = df.apply(lambda row: row['A'] + row['B'], axis=1)


# Create a sample DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
                   'Age': [25, 30, 35, 27, 30],
                   'City': ['New York', 'London', 'Paris', 'New York', 'London']})

# Drop duplicate rows based on all columns
df_unique = df.drop_duplicates()

# Drop duplicate rows based on specific columns
df_unique = df.drop_duplicates(['Name', 'City'])

# Drop duplicate rows and keep the last occurrence
df_unique = df.drop_duplicates(['Name', 'City'], keep='last')