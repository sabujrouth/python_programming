from itertools import count
import pyautogui
import time
time.sleep(5)
count=0
while count<=500:
    pyautogui.typewrite("I Love You So Much")
    pyautogui.press("Enter")
    count=count+1