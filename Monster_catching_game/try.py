# --Imports--
import random
import json

# --Styling--
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
BOLD = "\033[1m"
BG_WHITE   = "\033[47m"

# --Data--

# Input
choice = None

# Game variables
command = ""
crnt_city = ""
money = 0
mons_hp = 0
mons_evl_hp = 0

# Game lists
cities = ["vatica", "nethans", "luna", "suncity"]

# Game dictionaries
gym_won = {
    "Vatica": False,
    "Nethans": False,
    "Luna": False,
    "Suncity": False
}

plyr_info = {
    "name": "",
    "money": 0,
    "team": [],
    "gym_won": gym_won
}

item_quantity = {
    "potion": 0,
    "disk_space": 0,
}

item_price = {
    "potion": 10,
    "disk_space": 20
}

monster_bluprint = {
        "megmamon": {
        "name": "megmamon",
        "type": "Fire",
        "base_hp": random.randint(20, 25),
        "base_atk": random.randint(5, 10)
    },
    "splashermon": {
        "name": "splashermon",
        "type": "Water",
        "base_hp": random.randint(25, 30),
        "base_atk": random.randint(2, 10)
    },
    "bailsmon": {
        "name": "bailsmon",
        "type": "Grass",
        "base_hp": random.randint(25, 35),
        "base_atk": random.randint(2, 5)
    }
}

encountered_monster = {
    
}

monster_i_have = {

}

active_monster = {

}

print(f"{RED}--------------------------------{RESET}")

# --Functions--

def command_controls():
    global command
    command = input(f"{BOLD}>{RESET}").lower()
    
    

def new():
    print(f"{BOLD}Welcome to the Monster Catching Game!{RESET}")
    print(f"{ITALIC}In this game, you will embark on an exciting adventure to catch and train monsters.{RESET}")
    print(f"{ITALIC}You will travel through different cities, battle other trainers, and collect powerful monsters.{RESET}")
    print(f"{ITALIC}Your goal is to become the ultimate monster trainer!{RESET}")
    print(f"{ITALIC}Good luck on your journey!{RESET}")
    print(f"{BG_WHITE}{BLUE}help/tutorial - To look at the commands.{RESET}")
    command_controls()


def tutorial():
    print(f"{BG_WHITE}{BLUE}{BOLD}This is the tutorial for this game.{RESET}")
    print(f"{BG_WHITE}{BLUE}Since, you can not add controlls in vanilla python, This game will be controlled with a few commands that{RESET}")
    print(f"{BG_WHITE}{BLUE}It will be easy to understand, use and memorise. ;-){RESET}")
    print(f"{BG_WHITE}{BLUE}The commands are as follows:{RESET}")
    print(f"{BG_WHITE}{BLUE}1. {BOLD}{RESET}{BG_WHITE}{BLUE}load - If you have a saved game in the form of json.{RESET}")
    print(f"{BG_WHITE}{BLUE}2. {BOLD}{RESET}{BG_WHITE}{BLUE}save - Saves your current game progress.{RESET}")
    print(f"{BG_WHITE}{BLUE}3.{BOLD}{RESET}{BG_WHITE}{BLUE}catch - If you want to catch a monster.{RESET}")
    print(f"{BG_WHITE}{BLUE}4.{BOLD}{RESET}{BG_WHITE}{BLUE}buy - Can only be used in stores to buy stuff.{RESET}")
    print(f"{BG_WHITE}{BLUE}5.{BOLD}{RESET}{BG_WHITE}{BLUE}info - To have your info.{RESET}")
    print(f"{BG_WHITE}{BLUE}6.{BOLD}{RESET}{BG_WHITE}{BLUE}party - To Know who which monster is currently usable.{RESET}")
    print(f"{BG_WHITE}{BLUE}7.{BOLD}{RESET}{BG_WHITE}{BLUE}attack - To attack your enemy.{RESET}")
    print(f"{BG_WHITE}{BLUE}8.{BOLD}{RESET}{BG_WHITE}{BLUE}go - To go to buildings.{RESET}")
    print(f"{BG_WHITE}{BLUE}9.{BOLD}{RESET}{BG_WHITE}{BLUE}go_to - To travel a different place in map.{RESET}")
    print(f"{BG_WHITE}{BLUE}10.{BOLD}{RESET}{BG_WHITE}{BLUE}active - To see the current active monster.{RESET}")
    print(f"{BG_WHITE}{BLUE}11.{BOLD}{RESET}{BG_WHITE}{BLUE}activate - To change the current active monster.{RESET}")
    print(f"{BG_WHITE}{BLUE}12.{BOLD}{RESET}{BG_WHITE}{BLUE}Battle - To have a battle with other trainers and gym leaders.{RESET}")
    print(f"{BG_WHITE}{BLUE}13.{BOLD}{RESET}{BG_WHITE}{BLUE}item_info - To know the quantity of items you have.{RESET}")
    print(f"{BG_WHITE}{BLUE}14.{BOLD}{RESET}{BG_WHITE}{BLUE}help/tutorial - To look at the commands again.{RESET}")
    command_controls()

def map_management():
    global crnt_city
    global choice
    global cities
    crnt_city = "vatica"
    choice = input(f"{GREEN}Do you want to go somewhere? [Y/N] > {RESET}").lower()
    if choice == "y" :
        choice = input(f"{GREEN}Write where to go {cities} > {RESET}").lower()
        if choice in cities :
            crnt_city = choice
            print(crnt_city)

map_management()