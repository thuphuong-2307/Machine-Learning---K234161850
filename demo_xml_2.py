import pandas_read_xml as pdx

from data_processing.demo_xml import UelSample

df = pdx.read_xml("../dataset/SalesTransactions.xml", ['UelSample','SalesItem'])
print(df)
print(df.iloc[0])
data = df.iloc[0]

print(data)
print(data[0])
print(data[1]['OrderID'])