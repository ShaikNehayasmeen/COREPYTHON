import pandas as pd
from sqlalchemy import create_engine
username = 'root'
password = '1234'  
host = 'localhost' 
database = 'neha88'  
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'
engine = create_engine(connection_string)
df_sql = pd.read_sql('SELECT * FROM shopping_person', engine)
print("MySQL Data:")
print(df_sql.head()) 
csv_data = pd.read_csv('transactions.csv')  
print("\nCSV Data:")
print(csv_data.head()) 
merged_data = pd.merge(df_sql, csv_data, on='id', how='outer')
print("\nMerged Data:")
print(merged_data.head()) 
merged_data.to_csv('merged_customer_data.csv', index=False)

