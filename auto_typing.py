from itertools import count
import pyautogui
import time
time.sleep(5)
count = 0
while count <= 30:
    pyautogui.typewrite("hey")
    pyautogui.press("Enter")
    count = count+1
