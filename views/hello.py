import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from flask import *

# Player stat scraper ################################################
class Player:
	def __init__(self, name):
		self.name = name
		player = self.name

		letters = player[0:2]
		ini = player.split(" ")
		last = str(ini[1])
		last = last[0:5]
		ini = str(ini[1])
		ini = ini[0]

		self.url = 'https://www.basketball-reference.com/players/' + ini + '/' + last + letters +'01.html' 
		self.response = requests.get(self.url)
		self.soup = BeautifulSoup(self.response.text, "html.parser")
		

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
		return ret

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

	def printStats(self):
		print("\n")
		name = str(self.name)
		print("Player: " + name.upper() + "\n")
		print("PPG: " + self.ppg() + "\n")
		print("APG: " + self.apg() + "\n")
		print("RPG: " + self.rpg() + "\n")
		print("All-Stars: " + self.allStar() + "\n")
		print("Rings: " + self.finals() + "\n")

	# helper / mutator and getter methods

#name = input("What player stats would you like to retrieve?\n")
name = "steph curry"
player = Player(name)
player.__init__(name)
#player.printStats()


####### flask ####################
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "hello world"

@app.route('/player_stats')
def form():
	return render_template('player_stats.html')


@app.route('/player_stats', methods=['GET', 'POST'])
def form_post():
	ret = 5

	if request.method == 'POST':
		playerOneInput = request.form.get('playerOneName')
		playerTwoInput = request.form.get('playerTwoName')
		if playerOneInput != '':
			# player one 
			playerOneName = request.form['playerOneName']
			playerOne = Player(playerOneName)
			playerOne.__init__(playerOneName)
			fullName = playerOne.name
			points = playerOne.ppg()
			assists = playerOne.apg()
			playerOneStats = [fullName, points, assists]
			print("player one stats " + str(playerOneStats))
		if playerTwoInput != '':
			playerTwoName = request.form['playerTwoName']
			playerTwo = Player(playerTwoName)
			playerTwo.__init__(playerTwoName)
			fullName = playerTwo.name
			points = playerTwo.ppg()
			assists = playerTwo.apg()
			playerTwoStats = [fullName, points, assists]
			print("player two stats " + str(playerTwoStats))	
		return render_template('player_one_updated.html', playerOneStats = playerOneStats, playerTwoStats = playerTwoStats)
def player_ppg():
	ppg = player.ppg()
	return ppg
def player_apg():
	apg = player.apg()
	return apg