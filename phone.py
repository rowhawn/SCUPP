import pygame
import os

class Menu:
	def __init__(self, menuId, actionMessage, submenus = []):
		self.menuId = menuId
		self.actionMessage = actionMessage
		self.menuMessage = "you are in " + menuId
		self.submenus = submenus

	def readMenu(self):
		print(self.menuMessage)
		if (self.submenus[0] is not None):
			print("Press 1 to " + self.submenus[0].actionMessage)
		if (self.submenus[1] is not None):
			print("Press 2 to " + self.submenus[1].actionMessage)
		if (self.submenus[2] is not None):
			print("Press 3 to " + self.submenus[2].actionMessage)
		if (self.submenus[3] is not None):
			print("Press 4 to " + self.submenus[3].actionMessage)
		if (self.submenus[4] is not None):
			print("Press 5 to " + self.submenus[4].actionMessage)
		if (self.submenus[5] is not None):
			print("Press 6 to " + self.submenus[5].actionMessage)
		if (self.submenus[6] is not None):
			print("Press 7 to " + self.submenus[6].actionMessage)
		if (self.submenus[7] is not None):
			print("Press 8 to " + self.submenus[7].actionMessage)
		if (self.submenus[8] is not None):
			print("Press 9 to " + self.submenus[8].actionMessage)
		if (self.submenus[9] is not None):
			print("Press 0 to " + self.submenus[9].actionMessage)


homeDir = os.environ['HOME']
pygame.mixer.init()
pygame.mixer.music.load(homeDir + "/projects/SCUPP/resources/audio/match0.wav")
submenu1 = Menu("first submenu", "do the first action", [None, None, None, None, None, None, None, None, None, None])
submenu2 = Menu("second submenu", "do some other action", [None, None, None, None, None, None, None, None, None, None])
currMenu = Menu("main menu", "hear the main menu", [submenu1, submenu2, None, None, None, None, None, None, None, None]) 
submenu1.submenus[9] = currMenu
submenu2.submenus[9] = currMenu

while 1:
	currMenu.readMenu()
	keyPressed = input()
	if (keyPressed == '1' and currMenu.submenus[0] is not None):
                currMenu = currMenu.submenus[0]
                pygame.mixer.music.play(0)
	elif (keyPressed == '2' and currMenu.submenus[1] is not None):
		currMenu = currMenu.submenus[1]
	elif (keyPressed == '3' and currMenu.submenus[2] is not None):
		currMenu = currMenu.submenus[2]
	elif (keyPressed == '4' and currMenu.submenus[3] is not None):
		currMenu = currMenu.submenus[3]
	elif (keyPressed == '5' and currMenu.submenus[4] is not None):
		currMenu = currMenu.submenus[4]
	elif (keyPressed == '6' and currMenu.submenus[5] is not None):
		currMenu = currMenu.submenus[5]
	elif (keyPressed == '7' and currMenu.submenus[6] is not None):
		currMenu = currMenu.submenus[6]
	elif (keyPressed == '8' and currMenu.submenus[7] is not None):
		currMenu = currMenu.submenus[7]
	elif (keyPressed == '9' and currMenu.submenus[8] is not None):
		currMenu = currMenu.submenus[8]
	elif (keyPressed == '0' and currMenu.submenus[9] is not None):
		currMenu = currMenu.submenus[9]
	elif (keyPressed == '*'):
		print("you pressed something else!")
	elif (keyPressed == '#'):
		print("you pressed something else!")
	elif (keyPressed == 'quit'):
		quit()
	else:
		print("invalid input")

