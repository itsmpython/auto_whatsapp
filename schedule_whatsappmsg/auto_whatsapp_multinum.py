'''
This program sends whatsapp messages automatically to 
one or more numbers stored in the .csv file

NOTE: 
1. The .csv file must be located in the same folder as of this python program
2. Columns names in your .csv or gSheet should be labeled and ordered as followes ==>  'Name','Mob_Num'
3. You need to login to whatsapp web for the first time and stay logged in until the completion of the program
4. Use the following istructions to login to WhatsApp web
5. https://blog.whatsapp.com/whats-app-web#:~:text=To%20connect%20your%20web%20browser,with%20the%20WhatsApp%20web%20client.

'''
import time
import os
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import pandas as pd

keyboard = Controller()


def get_user_details():
    file_name = input("Enter the name of your .csv file : ")
    # Confirm the File path and name
    assert os.path.exists(
        file_name), "We could not find your file : "+str(file_name)
    f = open(file_name, 'r+')
    print("Hooray we found your file! : ", file_name)
    return file_name


def schedule_whatsapp_message(send_hour, send_min, phone_num, msg: str):
    country_code_prefix = '+'
    try:
        pywhatkit.sendwhatmsg(
            phone_no=country_code_prefix+str(phone_num),
            message=msg,
            time_hour=send_hour,
            time_min=send_min,
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


def pd_read_from_csv(csv_path):    # Extracting the data from local csv file
    csv_df = pd.read_csv(csv_path, usecols=['Name', 'Mob_Num'])
    return csv_df

'''
#NOTE : Commenting the Google sheet function for now as we won't be using it anytime in the near future

def pd_read_from_gsheet(sheet_id, sheet_name):  # If using google sheets

    # NOTE : Make sure the sheet is publically accessible
    sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    gsheet_df = pd.read_csv(sheet_url)
    return gsheet_df
'''


def send_whatsapp_message():
    msg = str(input('Please enter the message to be sent : '))
    print("Your messages will be queued up to be sent instantly. ")
    send_when = str(input("Would you like to schedule them instead? (Y/N) : "))
    if send_when == 'Y':
        print("NOTE : Scheduled messages may stop abruptly once the scheduled minute passes! ")
        send_hour = int(
            input('Please enter the schedule hour. Use 24 hour format : '))
        send_min = int(input('Please enter the schedule minutes : '))

    users_list = pd_read_from_csv(csv_path=get_user_details())
    print('Just came out of get_user_details function')
    user_name = users_list["Name"].values.tolist()

    for n in user_name:
        mob = users_list.query("Name == @n")["Mob_Num"]
        print(f'Mobile number of {n} is : {int(mob)}')
        #msg = f"Message to {n} from PythonScript!"
        print(msg)

        if send_when == 'N':
            
            whatsapp_instantly(mob, msg)  # To send the message instantly
        else:
            # To schedule the message
            schedule_whatsapp_message(send_hour, send_min, mob, msg)


if __name__ == "__main__":
    send_whatsapp_message()
