# pip install pywhatkit
from itertools import count
import pyautogui
import time
time.sleep(5)
count = 0
while count <= 1:
    pyautogui.typewrite("Hi")
    pyautogui.press("Enter")
    count = count+1