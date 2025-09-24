# Tra ve danh sach Khach hang co value giam dan
import sqlite3
import pandas as pd
try:
    # connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print("DB Init")
    # Write a query and excute it with cursor
    query = ("""SELECT c.CustomerId, sum(i.Total) as Total
                FROM Invoice as i 
                JOIN Customer as c 
                On c.CustomerId = i.CustomerId 
                GROUP BY i.CustomerId
                ORDER BY Total DESC
                LIMIT 50;""")
    cursor.execute(query)
    # Fetch and output result
    df = pd.DataFrame(cursor.fetchall())
    print(df)
#     Close the cursor
    cursor.close()
# Handle errors
except sqlite3.Error as error:
    print('Error occurred -', error)
# Close DB Connection irrespective of success of failure
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite Connection closed")

