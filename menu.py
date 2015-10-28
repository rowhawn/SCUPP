import pygame
from pygame.mixer import Sound
import time
from queue import Queue
import os
import glob
import csv

class Menu:
	def __init__(self, menuDir, prevMenu, menuPress):
		self.menuId = menuDir.split(os.sep)[-1][4:]
		self.parentMenu = prevMenu
		submenuDirs = [d for d in os.listdir(menuDir) if os.path.isdir(os.path.join(menuDir, d))]
		self.submenus = [None, None, None, None, None, None, None, None, None, self.parentMenu]
		try:
			self.actionMessage = pygame.mixer.Sound(glob.glob(menuDir + os.sep + 'action*')[0])
		except (IndexError, pygame.error):
			print('action message file not found or invalid format')
		try:
			self.menuMessage = pygame.mixer.Sound(glob.glob(menuDir + os.sep + 'menu*')[0])
		except (IndexError, pygame.error):
			print('menu message file not found or invalid format')
		self.menuPress = menuPress
		for submenuDir in submenuDirs:
			if submenuDir.startswith("1"):
				self.submenus[0] = Menu(menuDir + os.sep + submenuDir, self, self.menuPress)
			elif submenuDir.startswith("2"):
				self.submenus[1] = Menu(menuDir + os.sep + submenuDir, self, self.menuPress)
			elif submenuDir.startswith("3"):
				self.submenus[2] = Menu(menuDir + os.sep + submenuDir, self, self.menuPress)
			elif submenuDir.startswith("4"):
				self.submenus[3] = Menu(menuDir + os.sep + submenuDir, self, self.menuPress)
			elif submenuDir.startswith("5"):
				self.submenus[4] = Menu(menuDir + os.sep + submenuDir, self, self.menuPress)
			elif submenuDir.startswith("6"):
				self.submenus[5] = Menu(menuDir + os.sep + submenuDir, self, self.menuPress)
			elif submenuDir.startswith("7"):
				self.submenus[6] = Menu(menuDir + os.sep + submenuDir, self, self.menuPress)
			elif submenuDir.startswith("8"):
				self.submenus[7] = Menu(menuDir + os.sep + submenuDir, self, self.menuPress)
			elif submenuDir.startswith("9"):
				self.submenus[8] = Menu(menuDir + os.sep + submenuDir, self, self.menuPress)
			elif submenuDir.startswith("0"):
				self.submenus[9] = self.find_menu(self.parse_coordinate_file(menuDir + os.sep + submenuDir + os.sep + 'return.txt'))

	def read_menu(self, stopper, audioChannel):
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
				audioChannel.play(self.menuPress[index])
				if not stopper.empty():
					stopper.get()
					break
				audioChannel.queue(submenu.actionMessage)

	def find_root(self):
		if self.parentMenu is None:
			return self
		else:
			return self.parentMenu.find_root()

	def find_menu(self, coordinates):
		found_menu = self.find_root()
		for index in coordinates:
			try:
				found_menu = found_menu.submenus[index-1]
			except:
				print('no such menu found')
		return found_menu
			
	def parse_coordinate_file(self, filepath):
		coordinates = []
		with open(filepath, newline = '') as coordinate_file:
			reader = csv.reader(coordinate_file, delimiter=',')
			for row in reader:
				for number in row:
					coordinates.append(int(number))
		return coordinates
