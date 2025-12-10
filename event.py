import pyautogui
import time
pyautogui.FAILSAFE = False

while True:
    pyautogui.hotkey('scrolllock')
    print("yes")
    time.sleep(5)



# pyautogui.hotkey('scrolllock')
# pyautogui.press('scrolllock')