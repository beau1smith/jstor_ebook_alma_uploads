import pandas as pd
from datetime import datetime

d = pd.read_excel(open('test_input.xlsx', 'rb'), sheet_name='Additions')
df = pd.DataFrame(data=d)

#set options to display full dataframe information for QA purposes
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#to make a copy, add column names to new_df
#this pulls only the columns we need from the original sheet
new_df = df[[
    'titleSub',
    'EISBN',
    'PISBN',
    'Publisher Name',
    'DOI',
    'Copyright Year',
    'Authors'
    ]].copy()

#combine the title fields with the subtitles that aren't blank
#the pattern for the new title is "Title : Subtitle"

combine_cols = ['Title', 'Subtitle']
new_df['titleSub'] = new_df[combine_cols].apply(lambda x: ' : '.join(x.dropna()), axis=1)
print(new_df['titleSub'])

#add the fields required for the JSTOR eBooks Portfolio Loader Template
new_df['Localized'] = ''
new_df['Availability'] = 'ACTIVE'
new_df['PDA'] = 'jstor'

#combine the title fields with the subtitles that aren't blank
#the pattern for the new title is "Title : Subtitle"
combine_cols = ['Title', 'Subtitle']
new_df['titleSub'] = new_df[combine_cols].apply(lambda x: ' : '.join(x.dropna()), axis=1)

#update the DOI to include bkey prefix
new_df['DOI'] = 'bkey=' + new_df['DOI'].astype(str)

filedate = datetime.today().strftime('%m%d%Y')
filename = 'JSTOR_Portfolio_Loader' + filedate + ".xlsx"

#rename the columns to match the Alma upload spreadsheet
#new_df.rename(
#    columns={
#    'Title': 'OLD TITLE',
#    'Subtitle': ''}, inplace=True)

#new_df.to_excel(filename, columns=['Localized', 'EISBN', 'PISBN'])
