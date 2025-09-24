from bs4 import BeautifulSoup

# Reading the data inside the xml file to a variable under the name data
with open("../dataset/SalesTransactions.xml",'r') as file:
    data = file.read()

# Passing the stored data inside the beautifulsoup parser:
bs_data = BeautifulSoup(data,'xml')

# Finishing all instance of tag
UelSample = bs_data.find_all('UelSample')
print(UelSample)
