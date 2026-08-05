import json

# ==========================================
# 1. VARIABLES (Active Game State)
# ==========================================
current_city = "Pallet Town"
current_building = "Home"
player_money = 500
player_input = ""

# Combat Tracking Variables
current_player_mon_hp = 0
current_enemy_mon_hp = 0

# ==========================================
# 2. LISTS (Ordered Data)
# ==========================================
cities = ["Pallet Town", "Viridian City", "Pewter City"]

# List of monster dictionaries currently in team (max 6)
active_party = [
    {
        "id": "mon_001",
        "nickname": "Ignisaur",
        "level": 5,
        "current_hp": 20,
        "max_hp": 20,
        "moves": ["Tackle", "Ember"]
    }
]

# ==========================================
# 3. DICTIONARIES (Databases & Mappings)
# ==========================================
# Master blueprint for all species
all_monsters = {
    "mon_001": {"name": "Ignisaur", "type": "Fire", "base_hp": 20, "base_atk": 5},
    "mon_002": {"name": "Aqua-Lizard", "type": "Water", "base_hp": 22, "base_atk": 4}
}

# Wild/Catchable monsters available per route/area
available_monsters = {
    "Route 1": ["mon_001"],
    "Route 2": ["mon_001", "mon_002"]
}

# Shop items with prices and details
shop_catalog = {
    "Potion": {"price": 200, "heal_amount": 20},
    "Monster Capsule": {"price": 100, "catch_rate": 1.5}
}

# Player inventory (Item Name -> Quantity)
inventory = {
    "Potion": 3,
    "Monster Capsule": 5
}

# Track progression
gyms_won = {
    "Boulder Badge": False,
    "Cascade Badge": False
}

# General player information
player_info = {
    "name": "Red",
    "badges_count": 0,
    "is_in_battle": False
}

# Combined Save Data container for JSON export
save_data = {
    "player_info": player_info,
    "current_city": current_city,
    "money": player_money,
    "inventory": inventory,
    "active_party": active_party,
    "gyms_won": gyms_won
}

print("Game initialised successfully!")