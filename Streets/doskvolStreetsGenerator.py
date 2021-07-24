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


def rc(variable):
    """rc = random choice. Picks a random item from the list and returns
    it. This is mostly to shorten up the variables in the print command"""
    return random.choice(variable)


# Establish lists from json dumps
moods = json_retreiver("moods.json")
sights = json_retreiver("sights.json")
sounds = json_retreiver("sounds.json")
smells = json_retreiver("smells.json")
use = json_retreiver("use.json")
infastructure_type = json_retreiver("infastructure_type.json")
details = json_retreiver("details.json")

print(
    f"This {rc(moods)} {rc(infastructure_type)} is primarily used for {rc(use)}."
)
print(f"(A/An) {rc(sights).capitalize()} catch(es) your eye.")
print(f"You hear {rc(sounds)} and smell {rc(smells)} on the air.")
print(
    f"You can't help but notice {rc(details)} and {rc(details)}."
)
