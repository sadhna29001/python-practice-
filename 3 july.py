import pandas as pd

# Assuming 'df' is your DataFrame
df['column_with_nulls'] = df['column_with_nulls'].fillna(df['column_with_nulls'].mean())




import pandas as pd

# Assuming 'df' is your DataFrame
df['column_with_nulls'] = df['column_with_nulls'].fillna(df['column_with_nulls'].median())


import pandas as pd

# Assuming 'df' is your DataFrame
df['column_with_nulls'] = df['column_with_nulls'].fillna(df['column_with_nulls'].mode()[0])


import pandas as pd

# Assuming 'df' is your DataFrame
df['column_with_nulls'] = df['column_with_nulls'].fillna(df['column_with_nulls'].mode().max())


import pandas as pd

# Assuming 'df' is your DataFrame
df = df.dropna(subset=['column_with_nulls'])



import pandas as pd

# Assuming 'df' is your DataFrame
df['column_with_nulls'] = df['column_with_nulls'].interpolate()



import pandas as pd

# Assuming 'df' is your DataFrame
df['column_with_nulls'] = df['column_with_nulls'].fillna(df['column_with_nulls'].min())



import pandas as pd
from sklearn.impute import KNNImputer

# Assuming 'df' is your DataFrame
imputer = KNNImputer(n_neighbors=5)
df['column_with_nulls'] = imputer.fit_transform(df[['column_with_nulls']])



import pandas as pd
from fancyimpute import MICE

# Assuming 'df' is your DataFrame
imputer = MICE()
df['column_with_nulls'] = imputer.fit_transform(df[['column_with_nulls']])



import pandas as pd

# Create a sample DataFrame with null values
df = pd.DataFrame({'A': [1, 2, None, 4, None], 'B': [5, None, 7, 8, 9]})

# Check for null values
print(df.isnull().sum())
# Output:
# A    2
# B    1
# dtype: int64

# Drop rows with any null values
df_dropped = df.dropna()
print(df_dropped)
# Output:
#    A  B
# 0  1  5
# 3  4  8
# 4  NaN 9

# Fill null values with a specific value
df['A'] = df['A'].fillna(0)
df['B'] = df['B'].fillna(100)
print(df)
# Output:
#      A    B
# 0  1.0  5.0
# 1  2.0  100.0
# 2  0.0  7.0
# 3  4.0  8.0
# 4  0.0  9.0

# Forward fill null values
df['A'] = df['A'].fillna(method='ffill')
df['B'] = df['B'].fillna(method='ffill')
print(df)
# Output:
#      A    B
# 0  1.0  5.0
# 1  2.0  100.0
# 2  2.0  7.0
# 3  4.0  8.0
# 4  4.0  9.0

# Backward fill null values
df['A'] = df['A'].fillna(method='bfill')
df['B'] = df['B'].fillna(method='bfill')
print(df)
# Output:
#      A    B
# 0  1.0  5.0
# 1  2.0  100.0
# 2  4.0  7.0
# 3  4.0  8.0
# 4  NaN  9.0





import pandas as pd
from sklearn.impute import SimpleImputer

# Create a sample DataFrame with null values
df = pd.DataFrame({'A': [1, 2, None, 4, None], 'B': [5, None, 7, 8, 9]})

# Impute null values using the mean
imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print(df_imputed)
# Output:
#      A    B
# 0  1.0  5.0
# 1  2.0  7.5
# 2  2.5  7.0
# 3  4.0  8.0
# 4  2.5  9.0

# Impute null values using the median
imputer = SimpleImputer(strategy='median')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print(df_imputed)
# Output:
#      A    B
# 0  1.0  5.0
# 1  2.0  8.0
# 2  2.0  7.0
# 3  4.0  8.0
# 4  2.0  9.0

# Impute null values using the most frequent value
imputer = SimpleImputer(strategy='most_frequent')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print(df_imputed)
# Output:
#      A    B
# 0  1.0  5.0
# 1  2.0  8.0
# 2  2.0  7.0
# 3  4.0  8.0
# 4  2.0  9.0