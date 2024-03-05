from pynput import keyboard  # pip install pynput
import pyautogui             # pip install pyautogui
import csv
import os.path


start_position = 0
mid_position = 4000
prev_key = 'Key.ctrl'
flag = 'record'

# Recalling button positions from CSV file
if os.path.isfile('button_positions.csv'):
    csv_reader = csv.reader(open('button_positions.csv', 'r'))
    ob = list(csv_reader)
    dismiss = (int(ob[0][0]), int(ob[0][1]))
    verify = (int(ob[2][0]), int(ob[2][1]))
    confirm = (int(ob[4][0]), int(ob[4][1]))
    cancel = (int(ob[6][0]), int(ob[6][1]))
    # startEnd = (int(ob[8][0]), int(ob[8][1]))
else:  # If CSV file is absent
    dismiss = (700, 0)
    verify = (700, 0)
    confirm = (700, 0)
    cancel = (700, 0)
    startEnd = (0, 4000)
###################################################

print("\n Use 'Esc' key to kill the script instantly\n")
print("d = 'DISMISS' |   v = 'VERIFY' |   l = 'Verify CONFIRM' | c = 'Dismiss Confirm' \n")
print('Record button positions by keys \n"1" for DISMISS, "2" for VERIFY, "3" for VERIFY CONFIRM \
and "4" for DISMISS Confirm')


def on_press(key):
    global dismiss, verify, confirm, cancel, mid_position, prev_key, flag, start_position
    try:
        '''print('alphanumeric key {0} pressed'.format(
            key.char))'''

        if key.char == 'o' and flag == 'record':
            start_position = pyautogui.position()[0]
            print("\n \nNew Start-Position Recorded")
        if key.char == 'p' and flag == 'record':
            mid_position = pyautogui.position()[0]
            print("\n\n New End-Position Recorded")
        

        elif pyautogui.position()[0] > start_position and pyautogui.position()[0] < mid_position:
            if key.char == 'd':
                flag = ''
                pyautogui.click(dismiss)
            elif key.char == 'v':
                flag = ''
                pyautogui.click(verify)                
            elif key.char == 'l':
                pyautogui.click(confirm)
            elif key.char == 'c':
                pyautogui.click(cancel)
            
            else:
#                 if flag == 'record':
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
                with open('button_positions.csv', 'w+') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows([dismiss, verify, confirm, cancel])
        prev_key = "NULL"
        

    except AttributeError:
        print('special key {} pressed'.format(
            key))
        prev_key = str(key)


def on_release(key):
    global prev_key
    prev_key = key
    # print('{0} released'.format(
    #    key))
    if pyautogui.position()[0] > start_position and pyautogui.position()[0] < mid_position:
        if key == keyboard.Key.esc: # Stop listener            
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