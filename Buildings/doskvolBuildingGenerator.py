# doskvolBuildingGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random building. Use an argument of "rare" or "common" in the terminal

import random
import json
import sys


def json_retreiver(json_filename):
    """Call this from a variable with a filename string to populate
    with json content"""
    filename = json_filename
    with open(filename) as f:
        return json.load(f)


common_use = json_retreiver("common_use.json")
rare_use = json_retreiver("rare_use.json")
material = json_retreiver("material.json")
exterior_details = json_retreiver("exterior_details.json")
interior_details = json_retreiver("interior_details.json")

chosen_building = sys.argv[1]

if chosen_building == "rare":
    print(
        f"This {random.choice(exterior_details)} {random.choice(material)} {random.choice(rare_use)} is notable for it's {random.choice(interior_details)} and {random.choice(interior_details)}"
    )
elif chosen_building == "common":
    print(
        f"This {random.choice(exterior_details)} {random.choice(material)} {random.choice(common_use)} is notable for it's {random.choice(interior_details)} and {random.choice(interior_details)}"
    )
else:
    print("Please enter 'rare' or 'common' as an argument")
