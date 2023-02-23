import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import pandas as pd 

keyboard = Controller()

def schedule_whatsapp_message(phone_num, msg: str):
    try:
        pywhatkit.sendwhatmsg(
            phone_no="+919945508686", 
            message=msg,
            time_hour=16,
            time_min=50,
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

def pd_read_from_excel(sheet_path, sheet_name):    # If using the local excel file

    excel_df = pd.read_excel(sheet_path, sheet_name=sheet_name,usecols=['Name', 'Mob_Num'])
    return excel_df

def pd_read_from_gsheet(sheet_id, sheet_name): # If using the google sheet

    # Formatting the gSheet URL. Make sure the sheet is made publically accessible
    sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    gsheet_df = pd.read_csv(sheet_url)
    return gsheet_df

def whatsapp_to_num_frm_sheet(file_type):

    if file_type == 'excel':
        users_list = pd_read_from_excel(sheet_path='/Users/arjun/Development/python_environments/whatsapp/schedule_whatsappmsg/Whats_App_Msg_Receivers.xlsx',
                                    sheet_name='Receivers')
        user_name = users_list["Name"].values.tolist()
    elif file_type == 'gsheet':
        users_list = pd_read_from_gsheet(sheet_id = "1gpsLG9vD9Ra5It9UizqVqldCOLhDEPGgARzjQqQcg9Q", sheet_name = "Receivers")
        user_name = users_list["Name"].values.tolist()

    
    '''
    mobile_number = users_list["Mob_Num"].values.tolist()
    print(mobile_number)
    mobile = users_list.query("Name == 'Veerya'")["Mob_Num"]
    print(users_list.loc['Khalid', 'Mob_Num'])
    print('Mobile Number is ', int(mobile))
    '''

    for n in user_name:
        #print('Inside Loop Name is : ', n)
        mob = users_list.query("Name == @n")["Mob_Num"]
        print(f'Mobile number of {n} is : {int(mob)}')
        msg = f"Message to {n} from PythonScript!"
        print(msg)
        schedule_whatsapp_message(mob, msg)

        

if __name__ == "__main__":
    
    #schedule_whatsapp_message(msg="Test message from a Python script!")
    #pd_read_from_sheet(sheet_path = '/Users/arjun/Development/python_environments/whatsapp/schedule_whatsappmsg/Whats_App_Msg_Receivers.xlsx', sheet_name='Receivers')
    whatsapp_to_num_frm_sheet('excel')
