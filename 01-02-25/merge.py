import pandas as pd
cust_tran = pd.read_excel('df1.xlsx')
transactions = pd.read_csv('transactions.csv')
merged_df=pd.merge(cust_tran,transactions,on='id',how='outer')
merged_df.to_csv('merged_data.csv', index=False)
print(merged_df)