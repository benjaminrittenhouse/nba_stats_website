'''
Author: Benjamin Rittenhouse
https://github.com/benjaminrittenhouse
11/26/2020
main.py
Use of web scraper Player object and Flask framework to put stats from player to HTML file
'''

from flask import *
from Player import Player
####### flask ####################
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "hello world"

@app.route('/player_stats')
def form():
	return render_template('player_stats.html')

# main stat app route
@app.route('/player_stats', methods=['GET', 'POST'])
def form_post():
	ret = 5

	# user input from HTML post
	if request.method == 'POST':
		playerOneInput = request.form.get('playerOneName')
		playerTwoInput = request.form.get('playerTwoName')
		# if user entered player one
		if playerOneInput != '':
			# get name from html / create player object
			playerOneName = request.form['playerOneName']
			playerOneStats = getPlayerInfo(playerOneName)
		# if user entered player two
		if playerTwoInput != '':
			# get player name from html / create object
			playerTwoName = request.form['playerTwoName']
			playerTwoStats = getPlayerInfo(playerTwoName)

		tags = ["Player: ", "PPG: ", "APG: ", "RPG: ", "All Star Appearances: ", "Finals Wins: ", "Jersey Color: "]

		# error catching for if both, one, or none of fields are input (only returns stats for what is entered and refreshes page)
		if playerTwoInput != '' and playerOneInput != '':
			return render_template('player_one_updated.html', playerOneStats = playerOneStats, playerTwoStats = playerTwoStats)
		if playerTwoInput == '' and playerOneInput != '':
			return render_template('player_one_updated.html', playerOneStats = playerOneStats)
		if playerTwoInput != '' and playerOneInput == '':
			return render_template('player_one_updated.html', playerTwoStats = playerTwoStats)
		if playerOneInput == '' and playerTwoInput == '':
			return redirect(url_for('form_post'))

# method to get all stats of player and return in list to be posted to HTML
def getPlayerInfo(name):
	playerOneName = name
	playerOne = Player(playerOneName)
	playerOne.__init__(playerOneName)
	fullName = playerOne.name.upper()
	points = playerOne.ppg()
	assists = playerOne.apg()
	rebounds = playerOne.rpg()
	allStar = playerOne.allStar()
	finals = playerOne.finals()
	jerseyColor = playerOne.jerseyColor()
	playerOneStats = [fullName, points, assists, rebounds, allStar, finals, jerseyColor]
	return playerOneStats
