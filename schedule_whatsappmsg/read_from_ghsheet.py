#Use this code snippet if you just need to read the data from a Google Sheet

import pandas as pd

def read_receivers_from_gsheet(sheet_id, sheet_name):

    # Formatting the gSheet URL. Make sure the sheet is made publically accessible
    sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    excel_data_df = pd.read_csv(sheet_url)

    print(excel_data_df)



if __name__ == "__main__":

    read_receivers_from_gsheet(sheet_id = "1gpsLG9vD9Ra5It9UizqVqldCOLhDEPGgARzjQqQcg9Q", sheet_name = "Receivers")