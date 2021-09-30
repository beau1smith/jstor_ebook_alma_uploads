import pandas as pd
from datetime import datetime

additions = pd.read_excel(open('test_input.xlsx', 'rb'), sheet_name='Additions')
removals = pd.read_excel(open('test_input.xlsx', 'rb'), sheet_name='Removals')

additions_df = pd.DataFrame(data=additions)
removals_df = pd.DataFrame(data=removals)

#set options to display full dataframe information for QA purposes
#pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)

#Format the additions output

#combine the title fields with the subtitles that aren't blank
#the pattern for the new title is "Title : Subtitle"
combine_cols = ['Title', 'Subtitle']
additions_df['titleSub'] = additions_df[combine_cols].apply(lambda x: ' : '.join(x.dropna()), axis=1)


#add the fields required for the JSTOR eBooks Portfolio Loader Template
additions_df['localized'] = ''
additions_df['availability'] = 'ACTIVE'
additions_df['pda'] = 'jstor'

#update the DOI to include bkey prefix
additions_df['doi'] = 'bkey=' + additions_df['DOI'].astype(str)


#to make a copy, add column names to new_df
#this pulls only the columns we need from the original sheet
df_for_additions_upload = additions_df[[
    'localized',
    'EISBN',
    'PISBN',
    'titleSub',
    'availability',
    'Publisher Name',
    'Copyright Year',
    'doi',
    'Authors',
    'pda'
    ]].copy()

#rename the columns to match the Alma upload spreadsheet
df_for_additions_upload.rename(
    columns={
    'localized': 'LOCALIZED',
    'EISBN': 'ISBN',
    'PISBN': 'ISBN',
    'titleSub': 'TITLE',
    'availability': 'AVAILABILITY',
    'Publisher Name': 'PUBLISHER',
    'Copyright Year': 'DATE_OF_PUBLICATION',
    'doi': 'PARSER_PARAMETERS',
    'Authors': 'AUTHOR',
    'pda': 'PDA'}, inplace=True)

#add the fields required for the JSTOR eBooks Portfolio Loader Template


#combine the title fields with the subtitles that aren't blank
#the pattern for the new title is "Title : Subtitle"
#combine_cols = ['Title', 'Subtitle']
#new_df['titleSub'] = new_df[combine_cols].apply(lambda x: ' : '.join(x.dropna()), axis=1)

filedate = datetime.today().strftime('%m%d%Y')
additions_filename = 'JSTOR_Portfolio_Loader_' + filedate + '.xlsx'


#shape[0] counts the number of rows in the Additions tab of the spreadsheet
#if the additions tab has any rows of data, it will create an upload spreadsheet
if(df_for_additions_upload.shape[0] > 0):
    df_for_additions_upload.to_excel(additions_filename, index=False)

#format the removals output
df_for_removals_upload = removals_df[[
'EISBN',
'PISBN'
]].copy()

df_for_removals_upload.rename(
    columns={'EISBN':'ISBN', 'PISBN':'ISBN'},
    inplace=True)

removals_filename = 'JSTOR_Portfolio_Loader_' + filedate + '_DELETE.xlsx'

#shape[0] counts the number of rows in the Additions tab of the spreadsheet
#if the additions tab has any rows of data, it will create an upload spreadsheet
if(df_for_removals_upload.shape[0] > 0):
    df_for_removals_upload.to_excel(removals_filename, index=False)
