# nba_stats_website - Benjamin Rittenhouse

# About (Incomplete, 12/21/2020)
NBA Player Comparison Website
This website uses the Flask / Jinja web framework to allow a user to input two NBA players and get back statistics for each player, comparing them with bar graphs for each statistical category.

# Player object / Stat scraper
The Player.py is a python Player object that scrapes basketball-reference.com using the BeautifulSoup python module and its tagging system. This allows us to retrieve player points per game, rebounds per game, jersey color, etc. All credit for statistics go to basketball-reference.com and this website is not for profit in any way shape or form.

# main.py / the program
The main program basically gets information for a player and puts it in variables that are to be used on the HTML page through GET / POST forms. The form at the top of the page will allow the user to type a players name. To set the flask variable and run the program (Windows for me):
1. set FLASK_APP=main.py
2. run flask
I have been mainly running this in a virtual env with the modules all installed, noted at the top of the main.py and Player.py file.

# Stage
Currently, the site allows a user to input two player names, get back their PPG, APG, RPG, etc. and display it in a bar graph comparison. These graphs are also colored based on the color of the most recent jersey worn by the player, as also scraped from basketball-reference.com Future updates preferred:
- animate the graphs / make user interface cleaner
- allow drop down as person types name of player (to avoid typos / only let certain input)
- add further statistics
- add error catching such as someone enters a false player or only enters one player (or maybe force them to enter two players / change one at a time)
