# --Imports--
import random
import json

# --Data--

# Game variables
crnt_city = ""
money = 0
mons_hp = 0
mons_evl_hp = 0

# Game lists
Cities = ["Vatica", "Nethans", "Luna", "Suncity"]
Active_Monsters = []

# Game dictionaries
Gym_won = {
    "Vatica": False,
    "Nethans": False,
    "Luna": False,
    "Suncity": False
}

plyr_info = {
    "name": "",
    "money": 0,
    "team": []
}

