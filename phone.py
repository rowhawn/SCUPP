import pygame
from pygame.mixer import Sound, get_init, pre_init
import os
import glob
from threading import Thread
from note import Note
import time
from queue import Queue
from matrix_keypad import RPi_GPIO as keypad_GPIO

class Menu:
	def __init__(self, menuDir, prevMenu):
		self.menuId = menuDir.split(os.sep)[-1][4:]
		submenuDirs = [d for d in os.listdir(menuDir) if os.path.isdir(os.path.join(menuDir, d))]
		self.submenus = [None, None, None, None, None, None, None, None, None, prevMenu]
		#self.actionMessage = menuDir + os.sep + "action.wav"
		self.actionMessage = pygame.mixer.Sound(menuDir + os.sep + "action.wav")
		#self.menuMessage = menuDir + os.sep + "menu.wav"
		self.menuMessage = pygame.mixer.Sound(menuDir + os.sep + "menu.wav")
		for submenuDir in submenuDirs:
			if submenuDir.startswith("1"):
				self.submenus[0] = Menu(menuDir + os.sep + submenuDir, self)
			elif submenuDir.startswith("2"):
				self.submenus[1] = Menu(menuDir + os.sep + submenuDir, self)
			elif submenuDir.startswith("3"):
				self.submenus[2] = Menu(menuDir + os.sep + submenuDir, self)
			elif submenuDir.startswith("4"):
				self.submenus[3] = Menu(menuDir + os.sep + submenuDir, self)
			elif submenuDir.startswith("5"):
				self.submenus[4] = Menu(menuDir + os.sep + submenuDir, self)
			elif submenuDir.startswith("6"):
				self.submenus[5] = Menu(menuDir + os.sep + submenuDir, self)
			elif submenuDir.startswith("7"):
				self.submenus[6] = Menu(menuDir + os.sep + submenuDir, self)
			elif submenuDir.startswith("8"):
				self.submenus[7] = Menu(menuDir + os.sep + submenuDir, self)
			elif submenuDir.startswith("9"):
				self.submenus[8] = Menu(menuDir + os.sep + submenuDir, self)

	def read_menu(self, stopper):
		print("read menuMessage for " + self.menuId)
		audioChannel.play(self.menuMessage)
		for index, submenu in enumerate(self.submenus):
			if submenu is not None:
				while audioChannel.get_busy():
					time.sleep(0.1)
				if not stopper.empty(): 
					stopper.get()
					break
				print("read option " + str(index + 1) + ": " + submenu.menuId)
				if not stopper.empty():
					stopper.get()
					break
				audioChannel.play(menuPress[index])
				if not stopper.empty():
					stopper.get()
					break
				audioChannel.queue(submenu.actionMessage)

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
row1_tone.play(-1)
row1_tone.stop()

pygame.mixer.init()
audioChannel = pygame.mixer.Channel(0)

audioDir = os.getcwd() + os.sep + "resources" + os.sep + "audio"
os.chdir(audioDir)
clips = {}
for filename in glob.glob('*.wav'):
	clips[filename[:-4]] = pygame.mixer.Sound(filename)
menuPress = [clips['press1'], clips['press2'], clips['press3'], clips['press4'], clips['press5'], clips['press6'], clips['press7'], clips['press8'], clips['press9'], clips['press0']]

menuDir = audioDir + os.sep + "1 - Main Menu"
currMenu = Menu(menuDir, None)

def key_down(key):
	audioChannel.stop()
	stopQueue.put("stop")
	if key == 1:
		row1_tone.play(-1)
		col1_tone.play(-1)
	elif key == 2:
		row1_tone.play(-1)
		col2_tone.play(-1)
	elif key == 3:
		row1_tone.play(-1)
		col3_tone.play(-1)
	elif key == 4:
		row2_tone.play(-1)
		col1_tone.play(-1)
	elif key == 5:
		row2_tone.play(-1)
		col2_tone.play(-1)
	elif key == 6:
		row2_tone.play(-1)
		col3_tone.play(-1)
	elif key == 7:
		row3_tone.play(-1)
		col1_tone.play(-1)
	elif key == 8:
		row3_tone.play(-1)
		col2_tone.play(-1)
	elif key == 9:
		row3_tone.play(-1)
		col3_tone.play(-1)
	elif key == '*':
		row4_tone.play(-1)
		col1_tone.play(-1)
	elif key == 0:
		row4_tone.play(-1)
		col2_tone.play(-1)
	elif key == '#':
		row4_tone.play(-1)
		col3_tone.play(-1)

def key_up(key):
	global currMenu
	row1_tone.stop()
	row2_tone.stop()
	row3_tone.stop()
	row4_tone.stop()
	col1_tone.stop()
	col2_tone.stop()
	col3_tone.stop()
	print(str(key) + " was pressed")
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
		print("you pressed something else!")
	elif (key == '#'):
		print("you pressed something else!")
	elif (userInput == 'quit'):
		quit()
	else:
		print("invalid input")
	


lastKeyPressed = None
keyPressed = None
while 1:
	stopQueue = Queue()
	readMenuThread = Thread(target = currMenu.read_menu, args = (stopQueue,))
	readMenuThread.start()
	print('\n')
	
	while 1:
		keyPressed = kp.getKey()
		if lastKeyPressed == None and keyPressed != None:
			key_down(keyPressed)
		elif lastKeyPressed != None and keyPressed == None:
			key_up(lastKeyPressed)
			lastKeyPressed = keyPressed
			break
		lastKeyPressed = keyPressed
		time.sleep(0.05)
