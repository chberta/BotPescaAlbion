import pyautogui as pg
import cv2
import random
import numpy as np
from PIL import Image, ImageGrab
import time
#pega o retorno da posicao atual de x e y do mouse e passa o valor da tupla para as duas variaveis
print('Iniciando')
time.sleep(2)

meanvalue = 4.8

while True:
	arrayEND = True

	while arrayEND == True:
		time.sleep(0.3)
		catch = False
		window = ImageGrab.grab((837,532,1078,567)) #This is where the minigame will appear (FullHD)

		locate = pg.locate('obrezka.png',window, confidence = 0.6)
		if locate == None:
			break
		if locate != None:
			x = locate[0]
			print('x = '+ str(x) + ' catch = True')
			catch = True

		while catch == True:
			window = ImageGrab.grab((837,532,1078,567))
			ggmme = pg.locate('obrezka.png',window, confidence = 0.6)
			if ggmme != None:
				x = ggmme[0]
				print('x = '+ str(x) + '  has been found')
				if 65 < int(x) < 170:
					print('xxs')
					pg.mouseDown()
					time.sleep(1.2) #2
					pg.mouseUp()
					time.sleep(0.1)
				if int(x) < 64:
					pg.mouseDown()
					time.sleep(2.5)	#5
					pg.mouseUp()
			else:
				catch = False
				print('NONE')
				arrayEND = False
				print('minigame has been ended')
				time.sleep(5)
			


pass

# Copyright (c) 2020 Unbewohnte

