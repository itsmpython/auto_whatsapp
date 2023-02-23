#This program contain the core blocks that utilise pywhatkit, pyautogui and pynput packages and automate whatsapp messaging
#Blocks contain code to send whatsapp message instantly and also schedule


import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()

def send_whatsapp_message(msg: str):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no="+919945508686", 
            message=msg,
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

def schedule_whatsapp_message(msg: str):
    try:
        pywhatkit.sendwhatmsg(
            phone_no="+919945508686", 
            message=msg,
            time_hour=19,
            time_min=15,
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


if __name__ == "__main__":
    #send_whatsapp_message(msg="Test message from a Python script!")
    schedule_whatsapp_message(msg="Test message from a Python script!")