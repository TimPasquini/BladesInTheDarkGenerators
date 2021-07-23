# doskvolStreetsGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random city street.

import random
import json


def json_retreiver(json_filename):
    """Call this from a variable with a filename string to populate
    with json content"""
    filename = json_filename
    with open(filename) as f:
        return json.load(f)


# Call and print a mood for the street
moods = json_retreiver("moods.json")

# Impressions - sights, sounds, and smells
sights = json_retreiver("sights.json")
sounds = json_retreiver("sounds.json")
smells = json_retreiver("smells.json")

# Use - the purpose of the street
use = json_retreiver("use.json")

# Type -infastructure clasification
infastructure_type = json_retreiver("infastructure_type.json")

# Details - random supporting details
details = json_retreiver("details.json")

print(f"This street is {random.choice(moods)}.")
print(f"{random.choice(sights).capitalize()} catches your eye.")
print(f"You hear {random.choice(sounds)} and smell {random.choice(smells)}.")
print(f"The {random.choice(infastructure_type)} is primarily used for {random.choice(use)}.")
print(f"You can't help but notice {random.choice(details)} and {random.choice(details)}.")
