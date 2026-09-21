import pandas as pd

data_path = r'C:\Users\FM_pc\Desktop\E-commerce_dataset'

df = pd.read_csv(data_path + '\events.csv')

print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())

print(df['event_type'].unique())
print(df['event_type'].value_counts())
print(df['event_id'].duplicated().sum())
print(df['event_timestamp'].head())

test_time = pd.to_datetime(df['event_timestamp'],errors='coerce')
print(test_time.isnull().sum())
print(test_time.min())
print(test_time.max())
print(test_time.duplicated().sum())
print(test_time.sort_values().head())

print(df['event_type'].value_counts().sum())

print(df['user_id'].head())
print(df['user_id'].nunique())
print(df['user_id'].value_counts())

a = len(df)/df['user_id'].nunique()
print(a)

print(df['user_id'].str.len().value_counts())
print(df['user_id'].str.startswith('U').value_counts())
print(df['user_id'].str[1:].str.isnumeric().value_counts())

print(df['product_id'].str.len().value_counts())
print(df['product_id'].str[0].value_counts())
print(df['product_id'].str[1:].str.isnumeric().value_counts())

users = pd.read_csv(data_path + r'\users.csv')
print(users.columns)
print(users['user_id'].duplicated().sum())
print(df['user_id'].isin(users['user_id']).value_counts())

products = pd.read_csv(data_path + r'\products.csv')
print(products.columns)
print(products['product_id'].duplicated().sum())
print(df['product_id'].isin(products['product_id']).value_counts())