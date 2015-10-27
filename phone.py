import os
import glob
import time
import pygame
from enum import Enum
from queue import Queue
from threading import Thread
from note import Note
from menu import Menu
import RPi.GPIO as GPIO
from matrix_keypad import RPi_GPIO as keypad_GPIO
from pygame.mixer import Sound, get_init, pre_init

class Status(Enum):
	OFFHOOK = 1
	DIALING = 2
	CONNECTED = 3
	ONHOOK = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
				
kp = keypad_GPIO.keypad()
pre_init(44100, -16, 1, 1024)
pygame.init()
row1_tone = Note(697)
row2_tone = Note(770)
row3_tone = Note(852)
row4_tone = Note(941)
col1_tone = Note(1209)
col2_tone = Note(1336)
col3_tone = Note(1477)
dial_tone1 = Note(350)
dial_tone2 = Note(440)

pygame.mixer.init()
audioChannel = pygame.mixer.Channel(0)
audioChannel.set_volume(1.0)
toneChannel1 = pygame.mixer.Channel(1)
toneChannel1.set_volume(1.0)
toneChannel2 = pygame.mixer.Channel(2)
toneChannel2.set_volume(1.0)

audioDir = os.getcwd() + os.sep + "resources" + os.sep + "audio"
os.chdir(audioDir)

numbers_dialed = ''
clips = {}
phone_status = Status.ONHOOK
lastIsOnHook = True
isOnHook = True
lastKeyPressed = None
keyPressed = None

def key_down(key):
	global phone_status
	if phone_status == Status.CONNECTED:
		audioChannel.stop()
		stopQueue.put("stop")
	elif phone_status == Status.OFFHOOK:
		toneChannel1.stop()
		toneChannel2.stop()
		phone_status = Status.DIALING
		
	if key == 1:
		toneChannel1.play(row1_tone, -1)
		toneChannel2.play(col1_tone, -1)
	elif key == 2:
		toneChannel1.play(row1_tone, -1)
		toneChannel2.play(col2_tone, -1)
	elif key == 3:
		toneChannel1.play(row1_tone, -1)
		toneChannel2.play(col3_tone, -1)
	elif key == 4:
		toneChannel1.play(row2_tone, -1)
		toneChannel2.play(col1_tone, -1)
	elif key == 5:
		toneChannel1.play(row2_tone, -1)
		toneChannel2.play(col2_tone, -1)
	elif key == 6:
		toneChannel1.play(row2_tone, -1)
		toneChannel2.play(col3_tone, -1)
	elif key == 7:
		toneChannel1.play(row3_tone, -1)
		toneChannel2.play(col1_tone, -1)
	elif key == 8:
		toneChannel1.play(row3_tone, -1)
		toneChannel2.play(col2_tone, -1)
	elif key == 9:
		toneChannel1.play(row3_tone, -1)
		toneChannel2.play(col3_tone, -1)
	elif key == '*':
		toneChannel1.play(row4_tone, -1)
		toneChannel2.play(col1_tone, -1)
	elif key == 0:
		toneChannel1.play(row4_tone, -1)
		toneChannel2.play(col2_tone, -1)
	elif key == '#':
		toneChannel1.play(row4_tone, -1)
		toneChannel2.play(col3_tone, -1)

def key_up(key):
	global currMenu
	global phone_status
	global numbers_dialed
	toneChannel1.stop()
	toneChannel2.stop()
	print(str(key) + " was pressed")
	if phone_status == Status.DIALING:
		numbers_dialed += str(key)
		time.sleep(0.1)
	elif phone_status == Status.CONNECTED:
		time.sleep(0.5)		       
		if (key == 1):
			if (currMenu.submenus[0] is not None):
				currMenu = currMenu.submenus[0]
			else:
				print("No option for that number")
				audioChannel.play(clips['nooption'])
		elif (key == 2):
			if(currMenu.submenus[1] is not None):
				currMenu = currMenu.submenus[1]
			else:
				print("No option for that number")
				audioChannel.play(clips['nooption'])
		elif (key == 3):
			if(currMenu.submenus[2] is not None):
				currMenu = currMenu.submenus[2]
			else:
				print("No option for that number")
				audioChannel.play(clips['nooption'])
		elif (key == 4):
			if(currMenu.submenus[3] is not None):
				currMenu = currMenu.submenus[3]
			else:
				print("No option for that number")
				audioChannel.play(clips['nooption'])
		elif (key == 5):
			if(currMenu.submenus[4] is not None):
				currMenu = currMenu.submenus[4]
			else:
				print("No option for that number")
				audioChannel.play(clips['nooption'])
		elif (key == 6):
			if(currMenu.submenus[5] is not None):
				currMenu = currMenu.submenus[5]
			else:
				print("No option for that number")
				audioChannel.play(clips['nooption'])
		elif (key == 7):
			if(currMenu.submenus[6] is not None):
				currMenu = currMenu.submenus[6]
			else:
				print("No option for that number")
				audioChannel.play(clips['nooption'])
		elif (key == 8):
			if(currMenu.submenus[7] is not None):
				currMenu = currMenu.submenus[7]
			else:
				print("No option for that number")
				audioChannel.play(clips['nooption'])
		elif (key == 9):
			if(currMenu.submenus[8] is not None):
				currMenu = currMenu.submenus[8]
			else:
				print("No option for that number")
				audioChannel.play(clips['nooption'])
		elif (key == 0):
			if(currMenu.submenus[9] is not None):
				currMenu = currMenu.submenus[9]
			else:
				print("No option for that number")
				audioChannel.play(clips['nooption'])
		elif (key == '*'):
			print("No option for that key")
			audioChannel.play(clips['nooption'])
		elif (key == '#'):
			print("No option for that key")
			audioChannel.play(clips['nooption'])
		else:
			print("invalid input")
try:			
	while 1:
		if phone_status == Status.ONHOOK:
			if audioChannel.get_busy():
				audioChannel.stop()
				stopQueue.put("stop")
			if toneChannel1.get_busy():
				toneChannel1.stop()
			if toneChannel2.get_busy():
				toneChannel2.stop()   
		elif phone_status == Status.OFFHOOK:
			toneChannel1.play(dial_tone1, -1)
			toneChannel2.play(dial_tone2, -1)
		elif phone_status == Status.DIALING:
			if len(numbers_dialed) == 10:
				os.chdir(audioDir)
				if numbers_dialed in list(glob.glob('[0-9]10*')):
					print("connected!")
					phone_status = Status.CONNECTED
					phoneNumDir = audioDir + os.sep + numbers_dialed
					os.chdir(phoneNumDir)
					for filename in glob.glob('*.ogg'):
						clips[filename[:-4]] = pygame.mixer.Sound(filename)
					for filename in glob.glob('*.wav'):
						clips[filename[:-4]] = pygame.mixer.Sound(filename)
					menuPress = [clips['press1'], clips['press2'], clips['press3'], clips['press4'], clips['press5'], clips['press6'], clips['press7'], clips['press8'], clips['press9'], clips['press0']]
					menuDir = phoneNumDir + os.sep + "1 - Main Menu"
					currMenu = Menu(menuDir, None, menuPress)
				else:
					print("No such number exists!")
					phone_status = Status.OFFHOOK
					numbers_dialed = ''
				time.sleep(1)
				continue

		if phone_status == Status.CONNECTED:	      
			stopQueue = Queue()
			readMenuThread = Thread(target = currMenu.read_menu, args = (stopQueue, audioChannel,))
			while audioChannel.get_busy():
				time.sleep(0.1)
			readMenuThread.start()
			print('\n')

		while 1:
			GPIO.output(14, True)
			lastIsOnHook = isOnHook
			isOnHook = GPIO.input(15)
			if isOnHook and not lastIsOnHook:
				phone_status = Status.ONHOOK
				break
			elif not isOnHook and lastIsOnHook:
				phone_status = Status.OFFHOOK
				numbers_dialed = ''
				break
			if phone_status != Status.ONHOOK:
				keyPressed = kp.getKey()
				if lastKeyPressed == None and keyPressed != None:
					key_down(keyPressed)
				elif lastKeyPressed != None and keyPressed == None:
					key_up(lastKeyPressed)
					lastKeyPressed = keyPressed
					break
				lastKeyPressed = keyPressed
			time.sleep(0.05)
except KeyboardInterrupt:
	print('Quit from console, cleaning up GPIO')
finally:
	GPIO.cleanup()
