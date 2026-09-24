import pandas as pd

data_path = r'C:\Users\FM_pc\Desktop\E-commerce_dataset'
analysis_data = pd.read_csv(data_path + r'\analysis_data.csv')

# print(analysis_data.head())
# print(analysis_data.shape)
# print(analysis_data.dtypes)

analysis_data['order_date'] = pd.to_datetime(analysis_data['order_date'],errors='coerce')
# print(analysis_data.dtypes)

#------------------------
# monthly_orders
#------------------------
monthly_orders = analysis_data.groupby(['order_year', 'order_month'])['order_id'].nunique().rename('order_count')
monthly_orders = monthly_orders.reset_index()
# print(monthly_orders)
# print(monthly_orders.dtypes)
# monthly_orders = monthly_orders.sort_values('order_count',ascending=False)
# print(monthly_orders)
# print(monthly_orders.tail())

#------------------------
# product_sales
#------------------------
product_sales = analysis_data.groupby('product_id')['quantity'].sum()
product_sales = product_sales.reset_index()
product_sales = product_sales.sort_values('quantity',ascending=False)
# print(product_sales)

product_info = analysis_data[['product_id', 'product_name']].drop_duplicates()
product_sales = product_sales.merge(product_info,on='product_id',how='left')
product_sales = product_sales[['product_id','product_name','quantity']]

#------------------------
# top_10_products
#------------------------
top_10_products = product_sales.head(10)
# print(top_10_products)

#------------------------
# category_sales
#------------------------
category_sales = analysis_data.groupby('category')['quantity'].sum()
category_sales = category_sales.reset_index()
category_sales = category_sales.sort_values('quantity',ascending=False)
# print(category_sales)

#------------------------
# monthly_category_sales
#------------------------
monthly_category_sales = analysis_data.groupby(['order_year','order_month','category'])['quantity'].sum()
monthly_category_sales = monthly_category_sales.reset_index()
monthly_category_sales = monthly_category_sales.sort_values(['order_year','order_month','quantity'],ascending=[True,True,False])
# print(monthly_category_sales)

# monthly_top_category = monthly_category_sales.loc[monthly_category_sales.groupby(['order_year','order_month'])['quantity'].idxmax()]

monthly_category_sales['month'] = (monthly_category_sales['order_year'].astype(str) + '-' + monthly_category_sales['order_month'].astype(str).str.zfill(2))
# print(monthly_category_sales)

beauty_sales = monthly_category_sales[monthly_category_sales['category'] == 'Beauty']
# print(beauty_sales)

beauty_sales['previous_quantity'] = beauty_sales['quantity'].shift(1)
beauty_sales['quantity_change'] = (beauty_sales['quantity'] - beauty_sales['previous_quantity'])
beauty_sales = beauty_sales.sort_values('quantity_change',ascending=False)
# print(beauty_sales)

monthly_category_sales['previous_quantity'] = (
    monthly_category_sales
    .groupby('category')['quantity']
    .shift(1)
)
monthly_category_sales['quantity_change'] = (
    monthly_category_sales['quantity']
    - monthly_category_sales['previous_quantity']
)
monthly_category_sales = monthly_category_sales.sort_values(
    ['category','order_year','order_month']
)

# monthly_category_sales = monthly_category_sales.sort_values(
#     'quantity_change',
#     ascending=False
# )

# monthly_category_sales = monthly_category_sales.sort_values(
#     'quantity_change',
#     ascending=True
# )

# print(monthly_category_sales)
# print(
#     monthly_category_sales[
#         ['month', 'category', 'quantity', 'previous_quantity', 'quantity_change']
#     ]
# )

# print(monthly_category_sales.head(10))

monthly_category_sales_complete = monthly_category_sales[
    ~(
        (monthly_category_sales['order_year'] == 2025)
        & (monthly_category_sales['order_month'] == 11)
    )
]
# print(monthly_category_sales_complete.tail(10))

print(
    monthly_category_sales_complete[
        ['month', 'category', 'quantity', 'previous_quantity', 'quantity_change']
    ].sort_values(
        'quantity_change',
        ascending=True
    ).head(10)
)