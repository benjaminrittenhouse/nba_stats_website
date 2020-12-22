'''
Author: Benjamin Rittenhouse
https://github.com/benjaminrittenhouse
11/26/2020
Player.py
Web scraper used to get player stats from basketball-reference.com and put into Player object
'''

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from flask import *

# Player stat scraper #
class Player:
	def __init__(self, name):
		self.name = name
		player = self.name

		# get player URL Format
		letters = player[0:2]
		ini = player.split(" ")
		last = str(ini[1])
		last = last[0:5]
		ini = str(ini[1])
		ini = ini[0]

		# create url and use Beautiful Soup object
		self.url = 'https://www.basketball-reference.com/players/' + ini + '/' + last + letters +'01.html' 
		self.response = requests.get(self.url)
		self.soup = BeautifulSoup(self.response.text, "html.parser")
		
	# check if player has any all star appearances
	def allStar(self):
		allstar = self.soup.find("li", {"class": "all_star"})
		if str(allstar) != "None":
			allstar = str(allstar)
			ret = ""
			for L in allstar:
				if L.isdigit():
					ret += str(L)
			return ret
		else:
			ret = "None"
			return ret

	# check if player has any finals appearances
	def finals(self):
		ret = ""
		finals = self.soup.find("ul", {"id": "bling"})
		if 'NBA Champ' in str(finals):
			finals = finals.find_all('a')
			for x in str(finals).split("</a>"):
				if "NBA Champ" in x:
					for L in x:
						if L.isdigit():
							ret += str(L)
		if ret == "":
			return None
		else:
			return ret

	# check players ppg
	def ppg(self):
		wrap = self.soup.div
		p1 = wrap.find("div", {"class": "p1"})
		a = p1.find_all('p')
		rpg = a[3]
		string = str(rpg)
		string = string.split("<p>")
		string = str(string[1]).split("</p>")
		ret = string[0]
		return ret

	# check players rpg
	def rpg(self):
		wrap = self.soup.div
		p1 = wrap.find("div", {"class": "p1"})
		a = p1.find_all('p')
		rpg = a[5]
		string = str(rpg)
		string = string.split("<p>")
		string = str(string[1]).split("</p>")
		ret = string[0]
		return ret

	# check players apg
	def apg(self):
		wrap = self.soup.div
		p1 = wrap.find("div", {"class": "p1"})
		a = p1.find_all('p')
		rpg = a[7]
		string = str(rpg)
		string = string.split("<p>")
		string = str(string[1]).split("</p>")
		ret = string[0]
		return ret

	# debug to print player stats
	def printStats(self):
		print("\n")
		name = str(self.name)
		print("Player: " + name.upper() + "\n")
		print("PPG: " + self.ppg() + "\n")
		print("APG: " + self.apg() + "\n")
		print("RPG: " + self.rpg() + "\n")
		print("All-Stars: " + self.allStar() + "\n")
		print("Rings: " + self.finals() + "\n")

	#get player jersey color
	def jerseyColor(self):
		color = self.soup.find("div", {"class": "uni_holder bbr"})
		a = color.find_all('rect')
		string = str(a)
		string = string.split("</rect>")
		string = str(string[len(string) - 2])
		location = string.find("#")
		string = string[location:location+7]
		return string
