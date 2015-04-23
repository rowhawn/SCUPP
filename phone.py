import pygame
import os
import glob
from threading import Thread
import time
from queue import Queue

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

while 1:
	stopQueue = Queue()
	readMenuThread = Thread(target = currMenu.read_menu, args = (stopQueue,))
	readMenuThread.start()
	print('\n')
	userInput = input()
	if (userInput == '1'):
		audioChannel.stop()
		stopQueue.put("stop")
		if (currMenu.submenus[0] is not None):
			currMenu = currMenu.submenus[0]
		else:
			print("No option for that number")
			audioChannel.play(clips['nooption'])
	elif (userInput == '2'):
		audioChannel.stop()
		stopQueue.put("stop")
		if(currMenu.submenus[1] is not None):
			currMenu = currMenu.submenus[1]
		else:
			print("No option for that number")
			audioChannel.play(clips['nooption'])
	elif (userInput == '3'):
		audioChannel.stop()
		stopQueue.put("stop")
		if(currMenu.submenus[2] is not None):
			currMenu = currMenu.submenus[2]
		else:
			print("No option for that number")
			audioChannel.play(clips['nooption'])
	elif (userInput == '4'):
		audioChannel.stop()
		stopQueue.put("stop")
		if(currMenu.submenus[3] is not None):
			currMenu = currMenu.submenus[3]
		else:
			print("No option for that number")
			audioChannel.play(clips['nooption'])
	elif (userInput == '5'):
		audioChannel.stop()
		stopQueue.put("stop")
		if(currMenu.submenus[4] is not None):
			currMenu = currMenu.submenus[4]
		else:
			print("No option for that number")
			audioChannel.play(clips['nooption'])
	elif (userInput == '6'):
		audioChannel.stop()
		stopQueue.put("stop")
		if(currMenu.submenus[5] is not None):
			currMenu = currMenu.submenus[5]
		else:
			print("No option for that number")
			audioChannel.play(clips['nooption'])
	elif (userInput == '7'):
		audioChannel.stop()
		stopQueue.put("stop")
		if(currMenu.submenus[6] is not None):
			currMenu = currMenu.submenus[6]
		else:
			print("No option for that number")
			audioChannel.play(clips['nooption'])
	elif (userInput == '8'):
		audioChannel.stop()
		stopQueue.put("stop")
		if(currMenu.submenus[7] is not None):
			currMenu = currMenu.submenus[7]
		else:
			print("No option for that number")
			audioChannel.play(clips['nooption'])
	elif (userInput == '9'):
		audioChannel.stop()
		stopQueue.put("stop")
		if(currMenu.submenus[8] is not None):
			currMenu = currMenu.submenus[8]
		else:
			print("No option for that number")
			audioChannel.play(clips['nooption'])
	elif (userInput == '0'):
		audioChannel.stop()
		stopQueue.put("stop")
		if(currMenu.submenus[9] is not None):
			currMenu = currMenu.submenus[9]
		else:
			print("No option for that number")
			audioChannel.play(clips['nooption'])
	elif (userInput == '*'):
		print("you pressed something else!")
	elif (userInput == '#'):
		print("you pressed something else!")
	elif (userInput == 'quit'):
		quit()
	else:
		print("invalid input")

