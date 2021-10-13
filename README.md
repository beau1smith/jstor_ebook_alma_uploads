#jstor_ebook_alma_uploads
##README
This python script takes an excel file that takes a Books at JSTOR DDA corpus update and formats it as an import spreadsheet than can be imported into Ex Libris Alma to update JSTOR portfolio holdings.

The script uses the Pandas library to extract and manipulate the spreadsheet data to create a new excel file.

The script can be run from the command line with a single argument for one file at a time using the following syntax:

```
python3 transfer_spreadsheet.py [starting_file_name.xlsx]
```

