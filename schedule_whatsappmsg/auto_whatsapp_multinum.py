'''
This program sends whatsapp messages automatically to 
one or more numbers stored in the .csv file

NOTE: 
1. Name of the .csv file must be whatsapp_receivers.csv
2. Columns names in your .csv or gSheet should be labeled and ordered as followes ==>  'Name','Mob_Num'

'''

import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import pandas as pd

keyboard = Controller()

def schedule_whatsapp_message(phone_num, msg: str):
    country_code_prefix = '+'
    try:
        pywhatkit.sendwhatmsg(
            phone_no=country_code_prefix+str(phone_num),
            message=msg,
            time_hour=23,
            time_min=51,
            tab_close=True
        )
        time.sleep(10)

        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))


def whatsapp_instantly(phone_num, msg: str):
    country_code_prefix = '+'
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=country_code_prefix+str(phone_num),
            message=msg,
            tab_close=True
        )
        time.sleep(10)  # sleeps 10 seconds to ensure things are in place

        pyautogui.click()  # Clicks the send button on whatsapp web
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))


def pd_read_from_csv(csv_path):    # If using the local excel file

    # excel_df = pd.read_excel(sheet_path, sheet_name=sheet_name,usecols=['Name', 'Mob_Num'])
    # return excel_df

    excel_df = pd.read_csv(csv_path, usecols=['Name', 'Mob_Num'])
    return excel_df


def pd_read_from_gsheet(sheet_id, sheet_name):  # If using google sheets

    # NOTE : Make sure the sheet is publically accessible
    sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    gsheet_df = pd.read_csv(sheet_url)
    return gsheet_df


def whatsapp_to_num_frm_sheet(file_type):

    if file_type == 'csv':
        users_list = pd_read_from_csv(csv_path='../schedule_whatsappmsg/whatsapp_receivers.csv')
        user_name = users_list["Name"].values.tolist()

    elif file_type == 'gsheet':
        users_list = pd_read_from_gsheet(sheet_id="1gpsLG9vD9Ra5It9UizqVqldCOLhDEPGgARzjQqQcg9Q", sheet_name="Receivers")
        user_name = users_list["Name"].values.tolist()

    for n in user_name:
        mob = users_list.query("Name == @n")["Mob_Num"]
        print(f'Mobile number of {n} is : {int(mob)}')
        msg = f"Message to {n} from PythonScript!"
        print(msg)

        whatsapp_instantly(mob, msg) #To send the message instantly


if __name__ == "__main__":
    whatsapp_to_num_frm_sheet('csv')
