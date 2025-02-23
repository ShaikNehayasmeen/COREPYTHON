import pandas as pd
from sqlalchemy import create_engine
username = 'root'  
password = '1234' 
host = 'localhost' 
database = 'neha88' 
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'
engine = create_engine(connection_string)
df_sql = pd.read_sql('SELECT * FROM shopping_person', engine)
print(df_sql)