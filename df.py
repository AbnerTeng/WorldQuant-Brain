# %%
import pandas as pd

file = './price_to_volume.csv'

df = pd.read_csv(file)
print(df)
# %%
df.to_csv('decay=10.csv')
# %%
import pandas as pd

file = './test.csv'

df = pd.read_csv(file)
print(df)
