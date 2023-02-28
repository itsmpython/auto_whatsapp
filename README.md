
# WhatsApp message automater

**Automatically send one or more whatsapp messages without having to send them individually and without having the keep clicking on send button on whatsapp.**

*The program uses pywhatkit, pyautogui, pynput and pandas

## Features

1. Instantly send a Whatsapp message to one or more Contacts
2. Schedule a Whatsapp message to one or more Contacts
3. Automater sends also clicks on the whatsapp web send button. No manual intervention is required by the user

## Constraints
1. Currently the program supports only .csv file format where you can store the contact numbers, contact name and the message to be delivered. 
2. You'll need to open the whatsapp web once and login and ensure you are not logged out when the program set to run


## Instructions
1. You'll need to install the packages pywhatkit, pyautogui, pynput and pandas
2. The .csv file must be located in the same folder as of this python program
3. Columns names in your .csv or gSheet should be labeled and ordered as followes ==>  'Name','Mob_Num'
4. You need to login to whatsapp web for the first time and stay logged in until the completion of the program
5. Use the following istructions to login to WhatsApp web
6. https://blog.whatsapp.com/whats-app-web#:~:text=To%20connect%20your%20web%20browser,with%20the%20WhatsApp%20web%20client.
7. Now run the 'auto_whatsapp_multinum.py' program
   --> _ python3 auto_whatsapp_multinum.py_
