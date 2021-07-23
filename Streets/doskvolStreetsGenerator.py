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


# Establish lists from json dumps
moods = json_retreiver("moods.json")
sights = json_retreiver("sights.json")
sounds = json_retreiver("sounds.json")
smells = json_retreiver("smells.json")
use = json_retreiver("use.json")
infastructure_type = json_retreiver("infastructure_type.json")
details = json_retreiver("details.json")

print(
    f"This {random.choice(moods)} {random.choice(infastructure_type)} is primarily used for {random.choice(use)}."
)
print(f"(A/An) {random.choice(sights).capitalize()} catch(es) your eye.")
print(f"You hear {random.choice(sounds)} and smell {random.choice(smells)} on the air.")
print(
    f"You can't help but notice {random.choice(details)} and {random.choice(details)}."
)
