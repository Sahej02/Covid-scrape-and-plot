import pandas as pd 

df = pd.read_csv("covid_data.csv", header = 0, index_col = None)
print(df.to_markdown())