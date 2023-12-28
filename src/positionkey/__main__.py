"""
This script simulates the mouse clicks with keyboard's keys.
Buttons refer to 'DISMISS', 'VERIFY', 'CONFIRM' and 'CANCEL' buttons on Verification Portal.
Please record the button positions before using on a new system...
by numeric keys '1', '2', '3' and '4' for 'DISMISS' 'VERIFY', 'CONFIRM' and 'CANCEL' respectively.
Only alerts from 'Alert Feeds' and not "outstanding" are accessible as of now.
Sometimes button positions change due to varying length of alert title, re-record the button position in such cases.
d = 'DISMISS'  |   v = 'VERIFY'    |   l = 'CONFIRM'   | c = 'CANCEL'
"""

from pynput import keyboard  # pip install pynput

import pyautogui             # pip install pyautogui
import csv
import os.path

mid_position = 1920
prev_key = 'Key.ctrl'

# Recalling button positions from CSV file, if present
if os.path.isfile('click_positions.csv'):
    csv_reader = csv.reader(open('click_positions.csv', 'r'))
    ob = list(csv_reader)
    
    try: # Linux Kernel
        dismiss = (int(ob[0][0]), int(ob[0][1]))
        verify = (int(ob[1][0]), int(ob[1][1]))
        confirm = (int(ob[2][0]), int(ob[2][1]))
        cancel = (int(ob[3][0]), int(ob[3][1]))

    except: # Windows Kernel
        print('Windows Detected')
        dismiss = (int(ob[0][0]), int(ob[0][1]))
        verify = (int(ob[2][0]), int(ob[2][1]))
        confirm = (int(ob[4][0]), int(ob[4][1]))
        cancel = (int(ob[6][0]), int(ob[6][1]))

else:  # If CSV file is absent
    dismiss = (700, 0)
    verify = (700, 0)
    confirm = (700, 0)
    cancel = (700, 0)
###################################################

print("\nTo kill the script instantly , use 'Esc' key\n")
print("d = 'DISMISS' button  |   v = 'VERIFY' button    |   l = 'CONFIRM' button   | c = 'CANCEL' button\n")
print('Record button positions instantly by keys "1" for DISMISS, "2" for VERIFY, "3" for CONFIRM \
and "4" for CANCEL')


def on_press(key):    
    global dismiss, verify, confirm, cancel, mid_position, prev_key
    try:
        '''print('alphanumeric key {0} pressed'.format(
            key.char))'''

        if key.char == 'p' and prev_key == "Key.ctrl":
            mid_position = pyautogui.position()[0]
            print("New Partition Recorded")

        elif pyautogui.position()[0] < mid_position:
            if key.char == 'd':
                pyautogui.click(dismiss)
            elif key.char == 'v':
                pyautogui.click(verify)
            elif key.char == 'l':
                pyautogui.click(confirm)
            elif key.char == 'c':
                pyautogui.click(cancel)
            elif key.char == 'p' and prev_key == "Key.ctrl":
                mid_position = pyautogui.position()[0]
                print("New Mid-Position Recorded")
		        # mid_position = pyautogui.position()[0]
            else:
                if key.char == '1':
                    dismiss = pyautogui.position()
                    print('New location of DISMISS recorded')
                elif key.char == '2':
                    verify = pyautogui.position()
                    print('New location of VERIFY recorded')
                elif key.char == '3':
                    confirm = pyautogui.position()
                    print('New location of CONFIRM recorded')
                elif key.char == '4':
                    cancel = pyautogui.position()
                    print('New location of CANCEL recorded')
                with open('click_positions.csv', 'w+') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows([dismiss, verify, confirm, cancel])
        prev_key = "NULL"
        

    except AttributeError:
        print('special key {} pressed'.format(
            key))
        prev_key = str(key)


def on_release(key):
    prev_key = "NULL"
    # print('{0} released'.format(
    #    key))
    if pyautogui.position()[0] < mid_position:
        if key == keyboard.Key.esc:
            # Stop listener
            return False


# Collect events until released
with keyboard.Listener(on_press=on_press, 
                        on_release=on_release) as listener:
                        listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
                            on_press=on_press,
                            on_release=on_release)


listener.start()