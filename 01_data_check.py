import pandas as pd

data_path = r'C:\Users\FM_pc\Desktop\E-commerce_dataset'

# =========================
# events.csv
# =========================

# df = pd.read_csv(data_path + '\events.csv')

# print(df.columns)
# print(df.dtypes)
# print(df.isnull().sum())
# print(df.duplicated().sum())

# print(df['event_type'].unique())
# print(df['event_type'].value_counts())
# print(df['event_id'].duplicated().sum())
# print(df['event_timestamp'].head())

# test_time = pd.to_datetime(df['event_timestamp'],errors='coerce')
# print(test_time.isnull().sum())
# print(test_time.min())
# print(test_time.max())
# print(test_time.duplicated().sum())
# print(test_time.sort_values().head())

# print(df['event_type'].value_counts().sum())

# print(df['user_id'].head())
# print(df['user_id'].nunique())
# print(df['user_id'].value_counts())

# a = len(df)/df['user_id'].nunique()
# print(a)

# print(df['user_id'].str.len().value_counts())
# print(df['user_id'].str.startswith('U').value_counts())
# print(df['user_id'].str[1:].str.isnumeric().value_counts())

# print(df['product_id'].str.len().value_counts())
# print(df['product_id'].str[0].value_counts())
# print(df['product_id'].str[1:].str.isnumeric().value_counts())

# users = pd.read_csv(data_path + r'\users.csv')
# print(users.columns)
# print(users['user_id'].duplicated().sum())
# print(df['user_id'].isin(users['user_id']).value_counts())

# products = pd.read_csv(data_path + r'\products.csv')
# print(products.columns)
# print(products['product_id'].duplicated().sum())
# print(df['product_id'].isin(products['product_id']).value_counts())

# =========================
# users.csv
# =========================

users = pd.read_csv(data_path + r'\users.csv')
# print(users.columns)
# print(users.dtypes)
# print(users.isnull().sum())
# print(users.duplicated().sum())
# print(users['user_id'].duplicated().sum())
# print(users['user_id'].str.len().value_counts())
# print(users['user_id'].str.startswith('U').value_counts())
# print(users['user_id'].str[1:].str.isnumeric().value_counts())

# print(users['email'].duplicated().sum())
# print(users['email'].head(10))
# print(users['email'].isnull().sum())

# print(users['name'].head(10))
# print(users['name'].isnull().sum())
# print(users['name'].duplicated().sum())

# name_check = users.groupby('name')['user_id'].nunique()
# print(name_check[name_check > 1])

# print(users['gender'].value_counts())
# print(users['gender'].isnull().sum())

# print(users['city'].value_counts())
# print(users['city'].isnull().sum())
# print(users['city'].str.strip().equals(users['city']))
# print((users['city'] =='').sum())
# print((users['city'].str.strip() == '').sum())
# print(users['city'].str.len().value_counts().sort_index())
# print(users.loc[users['city'].str.len() <=6, 'city'])
# print(users.loc[users['city'].str.len() >=22, 'city'])

# print(users['signup_date'].head(10))
# print(users['signup_date'].isnull().sum())

signup_date = pd.to_datetime(users['signup_date'], errors='coerce')
print(signup_date.isnull().sum())
print(signup_date.min())
print(signup_date.max())
print(signup_date.dtype)
