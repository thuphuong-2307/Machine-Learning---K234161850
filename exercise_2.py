import pandas as pd

def find_orders_within_range(df, minValue, maxValue):
    # tổng giá trị từng đơn hàng
    order_totals = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
    # lọc đơn hàng trong range
    orders_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]
    # danh sách các mã đơn hàng không trùng nhau
    unique_orders = df[df['OrderID'].isin(orders_within_range.index)]['OrderID'].drop_duplicates().tolist()
    return unique_orders
def top_product(df):
    top3 = df.groupby('ProductID').apply(lambda x: (x['UnitPrice'] * x['Quantity']).sum())
    unique_products = df[df['ProductID'].isin(top3.index)]['ProductID'].drop_duplicates().tolist()

    return unique_products
df = pd.read_csv('../dataset/SalesTransactions.csv')

minValue = float(input("Nhập giá trị min: "))
maxValue = float(input("Nhập giá trị max: "))
result = find_orders_within_range(df, minValue, maxValue)
top = top_product(df)

print('Danh sách don hang:', result)
print("Top 3:",top)

