import pyautogui
import time
pyautogui.FAILSAFE = False

while True:
    pyautogui.hotkey('scrolllock')
    print("yes")
    time.sleep(5)