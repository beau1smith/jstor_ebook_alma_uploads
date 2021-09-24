import pandas as pd

d = pd.read_excel(open('test_input.xlsx', 'rb'), sheet_name='Additions')
df = pd.DataFrame(data=d)

#to make a copy, add column names to:
# new_df = df[['name1', 'name2', 'name3']].copy()
