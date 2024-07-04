import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

print("Original DataFrame:")
print(data.head())

data_one_hot = pd.DataFrame()

for unique_value in data['whoAmI'].unique():
    data_one_hot[unique_value] = (data['whoAmI'] == unique_value).astype(int)

print("\nOne-Hot Encoded DataFrame:")
print(data_one_hot.head())