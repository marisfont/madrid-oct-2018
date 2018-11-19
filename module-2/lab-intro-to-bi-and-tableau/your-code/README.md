# Lab | Introduction to BI and Tableau

## Data Set Import
- I opened the data set in a browser and added it to my Google Drive
- I launched the Tableau Public application and imported the data set from Google Sheets into Tableau
    - Connect sidebar > To a Server > Google Sheets
    - Loged into allowed Tableau to access my account
    - Selected the liquor_store_sales file and clicked Connect

## Data Set Interactions
- Changed the data type for  Year to string 
- Created a new field called Quarter by binning the month field using a bin size of 4.
    - Select month > Create > Bins
- Created a new worksheet 'Number of Records per Quarter':
    - With:
        - Quarter in the Rows section
        - Number of Records in the center of the view
    - Renamed the Quarters
        - Select Quarter > Aliases 
- Created new worksheets with tabular views for each of the following metrics:
    1. Total Retail Sales by Year/Quarter (rows).
    2. Average Retail Sales by Year/Quarter (rows).
    3. Total Retail Sales by Year/Month (rows) and Item Type (columns).
        - I had to create a copy of month in string format for the visual to make sense
    4. Average Retail Sales by Year/Month (rows) and Item Type (columns).
    5. Total Retail Transfers by Year/Quarter (rows).
    6. Average Retail Transfers by Year/Quarter (rows).
    7. Total Retail Transfers by Year/Month (rows) and Item Type (columns).
    8. Average Retail Transfers by Year/Month (rows) and Item Type (columns).
    9. Total Warehouse Sales by Year/Quarter (rows).
    10. Average Warehouse Sales by Year/Quarter (rows).
    11. Total Warehouse Sales by Year/Month (rows) and Item Type (columns).
    12. Average Warehouse Sales by Year/Month (rows) and Item Type (columns).
- I saved my work to Tableau Public and pasted the link to the main.txt document