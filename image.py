'''
Author: Benjamin Rittenhouse
https://github.com/benjaminrittenhouse
12/16/2020
image.py
Web scraper used to get player images from google search
'''

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from flask import *
		

firstName = "kyle"
lastName = "guy"
url = 'https://www.google.com/search?tbm=isch&source=hp&biw=1920&bih=966&ei=oTjaX5GQEYyOlwTZ4LrgDw&q=' + firstName + '+' + lastName + '&oq=' + firstName + '+' + lastName +'&gs_lcp=CgNpbWcQAzIFCAAQsQMyCAgAELEDEIMBMggIABCxAxCDATIICAAQsQMQgwEyBQgAELEDMggIABCxAxCDATIICAAQsQMQgwEyCAgAELEDEIMBMggIABCxAxCDATIICAAQsQMQgwE6AggAUIYZWNckYIsmaABwAHgAgAHYAYgBtgySAQUwLjYuM5gBAKABAaoBC2d3cy13aXotaW1n&sclient=img&ved=0ahUKEwjR5OvU-NLtAhUMx4UKHVmwDvwQ4dUDCAY&uact=5'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
found = soup.findAll("a", {"class":"wXeWr islib nfEiy mM5pbd"})
print(found)