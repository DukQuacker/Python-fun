#CS 50 Libraries 2/20/24 Zach Breazile
"""
import random #This could also be from random inport choise and that should act like a function so you won't need random

coin = random.choice(["heads", "tails"])

print(coin)
"""
'''
import random

cards = ["Jack", "Queen", "King"]

random.shuffle(cards)
for card in cards:
    print(card)
    '''
"""" 
import statistics

print(statistics.mean([100,90]))

"""

"""
try:
    print("Hello, my name is",sys.argv[1]) #if set to zero it will spit out the program name Example python3 day5.py it will spit out day5.py
except IndexError:
    print("Too few arguments")

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")


print("Hello, my name is",sys.argv[1])
"""
"""
for arg in sys.argv[1:-1]: #using slicing to take off the first element This should also remove the first element and the last one
    print("hello, my name is", arg)
"""

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])



