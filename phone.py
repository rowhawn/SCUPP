import pygame
import os
import glob

class Menu:
	def __init__(self, menuId, actionMessage, menuMessage, submenus = []):
		self.menuId = menuId;
		self.actionMessage = actionMessage
		self.menuMessage = menuMessage
		self.submenus = submenus

	def readMenu(self):
		print("read menuMessage for " + self.menuId)
		self.menuMessage.play()
		if (self.submenus[0] is not None):
			print("read option 1: " + self.submenus[0].menuId)
			clips['press1'].play()
			self.submenus[0].actionMessage.play()
		if (self.submenus[1] is not None):
			print("read option 2: " + self.submenus[1].menuId)
			clips['press2'].play()
			self.submenus[1].actionMessage.play()
		if (self.submenus[2] is not None):
			print("read option 3: " + self.submenus[2].menuId)
			clips['press3'].play()
			self.submenus[2].actionMessage.play()
		if (self.submenus[3] is not None):
			print("read option 4: " + self.submenus[3].menuId)
			clips['press4'].play()
			self.submenus[3].actionMessage.play()
		if (self.submenus[4] is not None):
			print("read option 5: " + self.submenus[4].menuId)
			clips['press5'].play()
			self.submenus[4].actionMessage.play()
		if (self.submenus[5] is not None):
			print("read option 6: " + self.submenus[5].menuId)
			clips['press6'].play()
			self.submenus[5].actionMessage.play()
		if (self.submenus[6] is not None):
			print("read option 7: " + self.submenus[6].menuId)
			clips['press7'].play()
			self.submenus[6].actionMessage.play()
		if (self.submenus[7] is not None):
			print("read option 8: " + self.submenus[7].menuId)
			clips['press8'].play()
			self.submenus[7].actionMessage.play()
		if (self.submenus[8] is not None):
			print("read option 9: " + self.submenus[8].menuId)
			clips['press9'].play()
			self.submenus[8].actionMessage.play()
		if (self.submenus[9] is not None):
			print("read option 0: " + self.submenus[9].menuId)
			clips['press0'].play()
			self.submenus[9].actionMessage.play()


homeDir = os.environ['HOME']
audioDir = homeDir + "/projects/SCUPP/resources/audio/"
os.chdir(audioDir)

pygame.mixer.init()
clips = {}
for filename in glob.glob('*.wav'):
	clips[filename[:-4]] = pygame.mixer.Sound(filename)

submenu1 = Menu("First Submenu", clips['submenu1actionmessage'], clips['submenu1menumessage'], [None, None, None, None, None, None, None, None, None, None])
submenu2 = Menu("Second Submenu", clips['submenu2actionmessage'], clips['submenu2menumessage'], [None, None, None, None, None, None, None, None, None, None])
submenu3 = Menu("Third Submenu", clips['submenu3actionmessage'], clips['submenu3menumessage'], [None, None, None, None, None, None, None, None, None, None])
submenu4 = Menu("Fourth Submenu", clips['submenu4actionmessage'], clips['submenu4menumessage'], [None, None, None, None, None, None, None, None, None, None])
submenu5 = Menu("Fifth Submenu", clips['submenu5actionmessage'], clips['submenu5menumessage'], [None, None, None, None, None, None, None, None, None, None])
submenu6 = Menu("Sixth Submenu", clips['submenu6actionmessage'], clips['submenu6menumessage'], [None, None, None, None, None, None, None, None, None, None])
submenu7 = Menu("Seventh Submenu", clips['submenu7actionmessage'], clips['submenu7menumessage'], [None, None, None, None, None, None, None, None, None, None])
submenu8 = Menu("Eighth Submenu", clips['submenu8actionmessage'], clips['submenu8menumessage'], [None, None, None, None, None, None, None, None, None, None])
submenu9 = Menu("Ninth Submenu", clips['submenu9actionmessage'], clips['submenu9menumessage'], [None, None, None, None, None, None, None, None, None, None])
mainMenu = Menu("Main Menu", clips['presspound'], clips['welcomemainmenu'], [submenu1, submenu2, submenu3, submenu4, submenu5, submenu6, submenu7, submenu8, submenu9, None])
mainMenu.submenus[9] = mainMenu
submenu1.submenus[9] = mainMenu
submenu2.submenus[9] = mainMenu
submenu3.submenus[9] = mainMenu
submenu4.submenus[9] = mainMenu
submenu5.submenus[9] = mainMenu
submenu6.submenus[9] = mainMenu
submenu7.submenus[9] = mainMenu
submenu8.submenus[9] = mainMenu
submenu9.submenus[9] = mainMenu
currMenu = mainMenu

while 1:
	currMenu.readMenu()
	print('\n')
	userInput = input()
	if (userInput == '1'):
		if (currMenu.submenus[0] is not None):
			currMenu = currMenu.submenus[0]
		else:
			print("No option for that number")
			clips['nooption'].play()
	elif (userInput == '2'):
		if(currMenu.submenus[1] is not None):
			currMenu = currMenu.submenus[1]
		else:
			print("No option for that number")
			clips['nooption'].play()
	elif (userInput == '3'):
		if(currMenu.submenus[2] is not None):
			currMenu = currMenu.submenus[2]
		else:
			print("No option for that number")
			clips['nooption'].play()
	elif (userInput == '4'):
		if(currMenu.submenus[3] is not None):
			currMenu = currMenu.submenus[3]
		else:
			print("No option for that number")
			clips['nooption'].play()
	elif (userInput == '5'):
		if(currMenu.submenus[4] is not None):
			currMenu = currMenu.submenus[4]
		else:
			print("No option for that number")
			clips['nooption'].play()
	elif (userInput == '6'):
		if(currMenu.submenus[5] is not None):
			currMenu = currMenu.submenus[5]
		else:
			print("No option for that number")
			clips['nooption'].play()
	elif (userInput == '7'):
		if(currMenu.submenus[6] is not None):
			currMenu = currMenu.submenus[6]
		else:
			print("No option for that number")
			clips['nooption'].play()
	elif (userInput == '8'):
		if(currMenu.submenus[7] is not None):
			currMenu = currMenu.submenus[7]
		else:
			print("No option for that number")
			clips['nooption'].play()
	elif (userInput == '9'):
		if(currMenu.submenus[8] is not None):
			currMenu = currMenu.submenus[8]
		else:
			print("No option for that number")
			clips['nooption'].play()
	elif (userInput == '0'):
		if(currMenu.submenus[9] is not None):
			currMenu = currMenu.submenus[9]
		else:
			print("No option for that number")
			clips['nooption'].play()
	elif (userInput == '*'):
		print("you pressed something else!")
	elif (userInput == '#'):
		print("you pressed something else!")
	elif (userInput == 'quit'):
		quit()
	else:
		print("invalid input")

