import pandas as pd
import random

# Generate the initial DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Display the first few rows of the initial DataFrame
print("Original DataFrame:")
print(data.head())

# Convert to one-hot encoding manually
data_one_hot = pd.DataFrame()

# Iterate through the unique values in the 'whoAmI' column and create one-hot columns
for unique_value in data['whoAmI'].unique():
    data_one_hot[unique_value] = (data['whoAmI'] == unique_value).astype(int)

# Display the one-hot encoded DataFrame
print("\nOne-Hot Encoded DataFrame:")
print(data_one_hot.head())