import pandas as pd
import numpy as np
data={'order_id':np.arange(1,1001)}
df=pd.DataFrame(data)
print(df['order_id'].dtype)
print(f"Memory usage:{df.memory_usage(deep=True)}")
df['order_id']=df['order_id'].astype(np.int16)
print(f"Memory Usage:{df.memory_usage(deep=True)}")