import pandas as pd

data_path = r'C:\Users\FM_pc\Desktop\E-commerce_dataset'

# =========================
# users.csv
# =========================

users = pd.read_csv(data_path + r'\users.csv')

users['signup_date'] = pd.to_datetime(users['signup_date'],errors='coerce')

# =========================
# orders.csv
# =========================

orders = pd.read_csv(data_path + r'\orders.csv')

orders['order_date'] = pd.to_datetime(orders['order_date'],errors='coerce')

# =========================
# reviews.csv
# =========================

reviews = pd.read_csv(data_path + r'\reviews.csv')

reviews['review_date'] = pd.to_datetime(reviews['review_date'],errors='coerce')

# =========================
# events.csv
# =========================

events = pd.read_csv(data_path + r'\events.csv')

events['event_timestamp'] = pd.to_datetime(events['event_timestamp'],errors='coerce')

# print(users.dtypes)
# print(orders.dtypes)
# print(reviews.dtypes)
# print(events.dtypes)

print(users['signup_date'].isnull().sum())
print(orders['order_date'].isnull().sum())
print(reviews['review_date'].isnull().sum())
print(events['event_timestamp'].isnull().sum())