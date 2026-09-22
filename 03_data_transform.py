import pandas as pd

data_path = r'C:\Users\FM_pc\Desktop\E-commerce_dataset'

# ========================= 
# orders.csv 
# =========================

orders = pd.read_csv(data_path + r'\orders.csv')

orders['order_date'] = pd.to_datetime(orders['order_date'],errors='coerce')
orders['order_year'] = orders['order_date'].dt.year
orders['order_month'] = orders['order_date'].dt.month

# print(orders.head())
# print(orders.dtypes)

# ========================= 
# order_items.csv 
# =========================

order_items = pd.read_csv(data_path + r'\order_items.csv')

# ========================== 
# 合併 orders + order_items 
# ==========================

order_items = orders.merge(order_items, on='order_id', how='inner')

# ========================== 
# 查看合併結果 
# ==========================
# print(order_items.head())
# print(order_items.shape)
# print(order_items.dtypes)

# print((order_items['user_id_x'] == order_items['user_id_y']).value_counts())

# =========================
# products.csv
# =========================

products = pd.read_csv( data_path + r'\products.csv')

# =========================
# 第二次合併
# order_items + products
# =========================

order_items = order_items.merge(products, on='product_id', how='inner')

# =========================
# 查看第二次合併結果
# =========================

# print(order_items.head())
# print(order_items.shape)
# print(order_items.dtypes)

# =========================
# 檢查 product_id 是否對應成功
# =========================

# print(order_items['product_id'].isin(products['product_id']).value_counts())

# =========================
# 整理分析用欄位
# =========================

analysis_data = order_items[
    [
        'order_date',
        'order_year',
        'order_month',
        'order_id',
        'product_id',
        'product_name',
        'category',
        'quantity',
        'item_total'
    ]
]

# =========================
# 查看最終分析資料
# =========================

print(analysis_data.head())
print(analysis_data.shape)
print(analysis_data.dtypes)
