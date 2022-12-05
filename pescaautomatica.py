'''
Funcionando 100%
'''
import pyautogui as pg
import cv2
import random
import numpy as np
from PIL import Image, ImageGrab
import time
#pega o retorno da posicao atual de x e y do mouse e passa o valor da tupla para as duas variaveis
print('Iniciando')
time.sleep(2)

print('Posicione o MOUSE Posição 1')
time.sleep(2)
xx, yy = pg.position()
print('Posicione o MOUSE Posição 2')
time.sleep(2)
xx1, yy1 = pg.position()
print('Posicione o MOUSE Posição 3')
time.sleep(2)
xx2, yy2 = pg.position()

print('Posicione o MOUSE Ponto Referencia')
time.sleep(2)
xx3, yy3 = pg.position()

x,y = 590,236
xtotalx = int()
xMEDx = float()
xQuantx = int()
xPop = float()
xPop1 = float()
xPop = 0
xMEDx = 0
xQuantx = 1
mediaArray = 0
xtotalx = 0
xtotalPesca= 0
xmen = 0
xMudLocal = 1

while True:

	pg.rightClick(xx3,yy3)

	arrayEND = False
	x, y = xx, yy

	if xMudLocal == 1:
		x, y = xx, yy
		xMudLocal = xMudLocal + 1
	elif xMudLocal == 2:
		x, y = xx1, yy1
		xMudLocal = xMudLocal + 1
	else:
		x, y = xx2, yy2
		xMudLocal = 1
			
	x = random.randint(x-10,x+10)
	y = random.randint(y-10,y+10)
	
	PrintImage = ImageGrab.grab((x-200,y-200,x+200,y+200))
	PrintImage.save('xii.png', 'BMP')
	PrintImageArray = cv2.imread('xii.png')
	PrintImageArrayG = np.array(PrintImageArray)
	PrinImageCalcula = cv2.Canny(PrintImageArrayG,90, 200)
	cv2.imwrite('aguaa.png', PrinImageCalcula)
	xmediaArray = np.mean(PrinImageCalcula) + 1.1
	xPop1 = np.mean(PrinImageCalcula)

	time.sleep(3.5)
	pg.moveTo(x , y) 
	pg.mouseDown()
	xtt = random.randint(2, 4)
	time.sleep(xtt / 10)
	pg.mouseUp()
	time.sleep(1.5)
	print('Pescar')
	time.sleep(0.5)

	while arrayEND == False:

		PrintdaImagem = ImageGrab.grab((x-200,y-200,x+200,y+200))

		if (xQuantx%2) == 0:
			PrintdaImagem.save('xi.png', 'BMP')
			PrintImageArrayOriginal = cv2.imread('xi.png')
		else:
			PrintdaImagem.save('xip.png', 'BMP')
			PrintImageArrayOriginal = cv2.imread('xip.png')

		
		PrintImageArrayG = np.array(PrintImageArrayOriginal)
		PrintImageAnalisa = cv2.Canny(PrintImageArrayG,90, 200)
		cv2.imwrite('agua.png', PrintImageAnalisa)
		PrintImage = np.mean(PrintImageAnalisa)
		

		if xPop == 0:
			xPop = xPop1 + np.mean(PrintImageAnalisa)
		else:
			xPop = xPop + np.mean(PrintImageAnalisa)

		xQuantx = xQuantx + 1
		
		
		mediaArray = (xPop / xQuantx) + 0.6
		print('Ponto Referencia parada= '+ str(mediaArray))
		print('Pontos Imagem = '+ str(PrintImage))
		time.sleep(0.3)


		if PrintImage == 0:
			print('Terminando Jogo')
			xPop = 0
			xQuantx = 1
			break
			
		if PrintImage >= float(mediaArray) and PrintImage != 0:
			time.sleep(0.1)
			pg.click(clicks = 2)
			arrayEND = True
			print('Fisgou ?')
			xQuantx = 1
			#time.sleep(2)
			xPop = 0
			break

		if xQuantx == 50:
			xPop = 0
			xQuantx = 1
			pg.click(clicks = 2)
			time.sleep(10)
			break


	while arrayEND == True:
		time.sleep(0.3)
		catch = False
		window = ImageGrab.grab((837,532,1078,567))

		locate = pg.locate('Boia.png',window, confidence = 0.5)
		if locate == None:
			break
		if locate != None:
			x = locate[0]
			print('Sx = '+ str(x) + ' catch = True')
			catch = True

		while catch == True:
			window = ImageGrab.grab((837,532,1078,567))
			ggmme = pg.locate('Boia.png',window, confidence = 0.5)
			if ggmme != None:
				x = ggmme[0]
				print('Fisgou Puxe x = '+ str(x) + '  Força')
				if 71 < int(x) < 170:
					pg.mouseDown()
					time.sleep(1.3)
					pg.mouseUp()
					
				if int(x) < 70:
					pg.mouseDown()
					time.sleep(2.5)	
					pg.mouseUp()
			else:
				catch = False
				print('NONE')
				arrayEND = False
				print('Pescaria Feita => ' +str(xtotalx))
				xtotalx = xtotalx + 1
				xtotalPesca = xtotalPesca + 1
				print('TotalPesca => ' +str(xtotalPesca))

				if xtotalPesca == 11:
					
					pg.hotkey('1')
					time.sleep(2.5)
					pg.rightClick(1594,557)		
					xtotalPesca = 0

				time.sleep(random.randint(10, 20))

pass

# Copyright (c) 2022 Chberta

