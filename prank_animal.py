import pyautogui as pg
import time

time.sleep(5)


txt = open('animals.txt','r')

a = "Sabuj is a "

for i in txt:
    pg.write(a+' '+i)
    pg.press('Enter')
