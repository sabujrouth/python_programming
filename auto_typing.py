from itertools import count
import pyautogui
import time
time.sleep(5)
count = 0
while count <= 100:
    pyautogui.typewrite("Gurudev")
    pyautogui.press("Enter")
    count = count+1