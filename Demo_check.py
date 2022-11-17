import pandas as pd
df = pd.read_excel('Retail.xlsx')
df.head()
#print(df)

df['LinePrice'] = df['Quantity'] * df['Unitprice']
df.head()
#print(df)

df_customers = df.groupby('CustomerID').agg(
    orders = ('InvoiceNo','nunique'),
    skus = ('Stockcode', 'nunique'),
    quantity = ('Quantity', 'sum'),
    revenue = ('LinePrice', 'sum'),
).reset_index()
df_customers.head()

print(df_customers)

