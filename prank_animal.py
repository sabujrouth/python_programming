import pyautogui as pg
import time

time.sleep(5)


txt = open('complement.txt','r')

a = ""

for i in txt:
    pg.write(a+' '+i)
    pg.press('Enter')