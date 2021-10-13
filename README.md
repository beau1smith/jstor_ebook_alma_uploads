# Reformatting data from JSTOR DDA weekly updates to Alma portfolio import spreadsheets 

This python script takes a single JSTOR DDA corpus excel spreadsheet as input and formats it as either an "Additions" or "Removals" spreadsheet than can be imported into Ex Libris Alma to update JSTOR ebook electronic portfolio holdings.

## Setup

1. Set up Pandas in your environment. This script was tested with Python 3.8.8 and Conda 4.10.1
2. Download git repository
```
   git clone https://github.com/beau1smith/jstor_ebook_alma_uploads.git
   cd jstor_ebook_alma_uploads
```
3. Save your JSTOR DDA excel file in the jstor_ebook_alma_uploads directory (or use test_input.xlsx)

## Usage

Run the script with a single argument
```
python3 transfer_spreadsheet.py [starting_file_name.xlsx]
```

The script uses the Pandas library to extract and manipulate the spreadsheet data to create a new excel file for each tab in the JSTOR DDA file. If there are no entries the "Additions" or "Removals" tab, the script will ignore that tab.

The template.xlsx file shows what the headings will look like:
* Localized will always be empty
* EISBN and PISBN from the input file are both renamed as ISBN fields
* Title and Subtitle fields are concatenated from the input into the Title field using the format [Title] : [Subtitle], if a subtitle exists
* Availability is always ACTIVE in all caps
* Publisher is the Publisher field from the input file
* Date_of_Publication is the Copyright Year from the input file
* Parser Paramters is BKEY=[DOI field from input]
* Author is Authors from the input file
* PDA is always jstor

## License
MIT License

