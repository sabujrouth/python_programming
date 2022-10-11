from itertools import count
import pyautogui
import time
time.sleep(5)
count=0
while count<=10:
    pyautogui.typewrite("Hello World!")
    pyautogui.press("Enter")
    count=count+1