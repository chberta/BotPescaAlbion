import pyautogui as pg
import time

print('Posicione o MOUSE')
time.sleep(2)
xx, yy = pg.position()

print ("x = "+str(xx)+" y = "+str(yy))
