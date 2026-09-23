import pandas as pd

data_path = r'C:\Users\FM_pc\Desktop\E-commerce_dataset'
analysis_data = pd.read_csv(data_path + r'\analysis_data.csv')

# print(analysis_data.head())
# print(analysis_data.shape)
# print(analysis_data.dtypes)

# analysis_data['order_date'] = pd.to_datetime(analysis_data['order_date'],errors='coerce')
# print(analysis_data.dtypes)

monthly_orders = analysis_data.groupby(['order_year', 'order_month'])['order_id'].nunique().rename('order_count')
monthly_orders = monthly_orders.reset_index()
# print(monthly_orders)
# print(monthly_orders.dtypes)
monthly_orders = monthly_orders.sort_values('order_count',ascending=False)
print(monthly_orders)
print(monthly_orders.tail())