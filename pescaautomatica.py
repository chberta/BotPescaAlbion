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

print('Posicione o MOUSE')
time.sleep(2)
xx, yy = pg.position()
print('Posicione o MOUSE 1')
time.sleep(2)
xx1, yy1 = pg.position()
print('Posicione o MOUSE 2')
time.sleep(2)
xx2, yy2 = pg.position()

print('Posicione o MOUSE Marca')
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
meanvalue = 8.5
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
	#pg.rightClick(x,y)


	poplavokplace = ImageGrab.grab((x-200,y-200,x+200,y+200)) #Takes a screenshot of the box where the float is 
	poplavokplace.save('xii.png', 'BMP')
	poplavok_place_image_original = cv2.imread('xii.png')
	poplavok_place_array = np.array(poplavok_place_image_original)
	poplavok_canny = cv2.Canny(poplavok_place_array,90, 200)
	cv2.imwrite('aguaa.png', poplavok_canny)
	xmeanvalue = np.mean(poplavok_canny) + 1.1
	xPop1 = np.mean(poplavok_canny)

	time.sleep(3.5)
	pg.moveTo(x , y)  #pg.moveTo(x , y, duration = 0.5) 
	pg.mouseDown()
	xtt = random.randint(2, 4)
	time.sleep(xtt / 10)
	pg.mouseUp()
	time.sleep(1.5)
	print('Pescar')
	time.sleep(0.5)

	while arrayEND == False:

		poplavokplace = ImageGrab.grab((x-200,y-200,x+200,y+200))

		if (xQuantx%2) == 0:
			poplavokplace.save('xi.png', 'BMP')
			poplavok_place_image_original = cv2.imread('xi.png')
		else:
			poplavokplace.save('xip.png', 'BMP')
			poplavok_place_image_original = cv2.imread('xip.png')

		#poplavok_place_image_original = cv2.imread('xi.png')
		poplavok_place_array = np.array(poplavok_place_image_original)
		poplavok_canny = cv2.Canny(poplavok_place_array,90, 200)
		cv2.imwrite('agua.png', poplavok_canny)
		poplavok_place_array_mean = np.mean(poplavok_canny)
		

		if xPop == 0:
			xPop = xPop1 + np.mean(poplavok_canny)
		else:
			xPop = xPop + np.mean(poplavok_canny)

		#print('Xpop= '+ str(xPop/xQuantx))
		 	
		xQuantx = xQuantx + 1
		
		
		meanvalue = (xPop / xQuantx) + 0.6
		print('Ponto Referencia parada= '+ str(meanvalue))
		print('Pontos Imagem = '+ str(poplavok_place_array_mean))
		#print('xQuantx = '+ str(xQuantx))
		#print('------------------')
		time.sleep(0.3)


		if poplavok_place_array_mean == 0:
			print('mean == 0, ending the program')
			xPop = 0
			xQuantx = 1
			break
			
		if poplavok_place_array_mean >= float(meanvalue) and poplavok_place_array_mean != 0:
			#time.sleep(2)
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
		window = ImageGrab.grab((837,532,1078,567)) #This is where the minigame will appear (FullHD)

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
					time.sleep(1.3)#1
					pg.mouseUp()
					#time.sleep(0.1)
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

				#time.sleep(10)
				time.sleep(random.randint(10, 20))

pass

# Copyright (c) 2020 Unbewohnte

