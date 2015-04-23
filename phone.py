#import pygame
import os
import glob

class Menu:
	def __init__(self, menuDir, prevMenu):
		self.menuId = menuDir.split(os.sep)[-1][4:]
		submenuDirs = [d for d in os.listdir(menuDir) if os.path.isdir(os.path.join(menuDir, d))]
		self.submenus = [None, None, None, None, None, None, None, None, None, prevMenu]
		self.actionMessage = menuDir + os.sep + "action.wav"
		#self.actionMessage = pygame.mixer.Sound(menuDir + os.sep + "action.wav")
		self.menuMessage = menuDir + os.sep + "menu.wav"
		#self.menuMessage = pygame.mixer.Sound(menuDir + os.sep + "menu.wav")
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

	def read_menu(self):
		print("read menuMessage for " + self.menuId)
		print(self.menuMessage)
		#self.menuMessage.play()
		if (self.submenus[0] is not None):
			print("read option 1: " + self.submenus[0].menuId)
			print(self.submenus[0].actionMessage)
			#clips['press1'].play()
			#self.submenus[0].actionMessage.play()
		if (self.submenus[1] is not None):
			print("read option 2: " + self.submenus[1].menuId)
			print(self.submenus[1].actionMessage)
			#clips['press2'].play()
			#self.submenus[1].actionMessage.play()
		if (self.submenus[2] is not None):
			print("read option 3: " + self.submenus[2].menuId)
			print(self.submenus[2].actionMessage)
			#clips['press3'].play()
			#self.submenus[2].actionMessage.play()
		if (self.submenus[3] is not None):
			print("read option 4: " + self.submenus[3].menuId)
			print(self.submenus[3].actionMessage)
			#clips['press4'].play()
			#self.submenus[3].actionMessage.play()
		if (self.submenus[4] is not None):
			print("read option 5: " + self.submenus[4].menuId)
			print(self.submenus[4].actionMessage)
			#clips['press5'].play()
			#self.submenus[4].actionMessage.play()
		if (self.submenus[5] is not None):
			print("read option 6: " + self.submenus[5].menuId)
			print(self.submenus[5].actionMessage)
			#clips['press6'].play()
			#self.submenus[5].actionMessage.play()
		if (self.submenus[6] is not None):
			print("read option 7: " + self.submenus[6].menuId)
			print(self.submenus[6].actionMessage)
			#clips['press7'].play()
			#self.submenus[6].actionMessage.play()
		if (self.submenus[7] is not None):
			print("read option 8: " + self.submenus[7].menuId)
			print(self.submenus[7].actionMessage)
			#clips['press8'].play()
			#self.submenus[7].actionMessage.play()
		if (self.submenus[8] is not None):
			print("read option 9: " + self.submenus[8].menuId)
			print(self.submenus[8].actionMessage)
			#clips['press9'].play()
			#self.submenus[8].actionMessage.play()
		if (self.submenus[9] is not None):
			print("read option 0: " + self.submenus[9].menuId)
			print(self.submenus[9].actionMessage)
			#clips['press0'].play()
			#self.submenus[9].actionMessage.play()

audioDir = os.getcwd() + os.sep + "resources" + os.sep + "audio"
os.chdir(audioDir)
menuDir = audioDir + os.sep + "1 - Main Menu"
currMenu = Menu(menuDir, None)

#pygame.mixer.init()
#clips = {}
#for filename in glob.glob('*.wav'):
#	clips[filename[:-4]] = pygame.mixer.Sound(filename)

while 1:
	currMenu.read_menu()
	print('\n')
	userInput = input()
	if (userInput == '1'):
		if (currMenu.submenus[0] is not None):
			currMenu = currMenu.submenus[0]
		else:
			print("No option for that number")
			#clips['nooption'].play()
	elif (userInput == '2'):
		if(currMenu.submenus[1] is not None):
			currMenu = currMenu.submenus[1]
		else:
			print("No option for that number")
			#clips['nooption'].play()
	elif (userInput == '3'):
		if(currMenu.submenus[2] is not None):
			currMenu = currMenu.submenus[2]
		else:
			print("No option for that number")
			#clips['nooption'].play()
	elif (userInput == '4'):
		if(currMenu.submenus[3] is not None):
			currMenu = currMenu.submenus[3]
		else:
			print("No option for that number")
			#clips['nooption'].play()
	elif (userInput == '5'):
		if(currMenu.submenus[4] is not None):
			currMenu = currMenu.submenus[4]
		else:
			print("No option for that number")
			#clips['nooption'].play()
	elif (userInput == '6'):
		if(currMenu.submenus[5] is not None):
			currMenu = currMenu.submenus[5]
		else:
			print("No option for that number")
			#clips['nooption'].play()
	elif (userInput == '7'):
		if(currMenu.submenus[6] is not None):
			currMenu = currMenu.submenus[6]
		else:
			print("No option for that number")
			#clips['nooption'].play()
	elif (userInput == '8'):
		if(currMenu.submenus[7] is not None):
			currMenu = currMenu.submenus[7]
		else:
			print("No option for that number")
			#clips['nooption'].play()
	elif (userInput == '9'):
		if(currMenu.submenus[8] is not None):
			currMenu = currMenu.submenus[8]
		else:
			print("No option for that number")
			#clips['nooption'].play()
	elif (userInput == '0'):
		if(currMenu.submenus[9] is not None):
			currMenu = currMenu.submenus[9]
		else:
			print("No option for that number")
			#clips['nooption'].play()
	elif (userInput == '*'):
		print("you pressed something else!")
	elif (userInput == '#'):
		print("you pressed something else!")
	elif (userInput == 'quit'):
		quit()
	else:
		print("invalid input")

