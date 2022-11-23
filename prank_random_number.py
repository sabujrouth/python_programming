import pyautogui as gui
import time
import random
import string

number = input(" Enter the number: ")


time.sleep(5)

for i in range(int(number)):
    stri = string.ascii_lowercase
    message = "".join(random.sample(stri, 10))
    gui.typewrite(message)
    gui.press(' Enter')