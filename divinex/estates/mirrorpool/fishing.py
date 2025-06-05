# mirrorpool/fishing.py

import random

class OfferingPool:
    def __init__(self):
        self.loot_table = {
            "Echo Scale": 0.3,
            "Fragmented Memory": 0.2,
            "Whispering Shell": 0.15,
            "Cursed Trinket": 0.1,
            "Godmarked Relic": 0.05,
            "Nothing": 0.2
        }

    def cast_line(self):
        roll = random.random()
        cumulative = 0.0
        for item, chance in self.loot_table.items():
            cumulative += chance
            if roll <= cumulative:
                return f"You pulled from the Offering Pool: {item}"
        return "The water rejected your offering."

    def adjust_loot(self, item, new_chance):
        if item in self.loot_table:
            self.loot_table[item] = new_chance
            return f"Loot table updated: {item} now has {new_chance*100}% chance"
        return "Item not found in pool."

    def view_loot_table(self):
        return self.loot_table