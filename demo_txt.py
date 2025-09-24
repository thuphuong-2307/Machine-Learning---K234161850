import pandas as pd
df = pd.read_csv('../dataset/SalesTransactions.txt',
                 # endcoding='utf-8', dtype='unicode',
                 sep='\t') # bo khoang cach

print(df)
