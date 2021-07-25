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


def print_street():
    """This will print text describing a random street"""
    print(
        f"""
    This {rc(moods)} {rc(infastructure_type)} is primarily used for {rc(use)}.
    (A/An) {rc(sights).capitalize()} catch(es) your eye. You hear {rc(sounds)} 
    and smell {rc(smells)} on the air. You can't help but notice 
    {rc(details)} and {rc(details)}."""
    )


# Establish lists from json dumps
moods = json_retreiver("Streets/moods.json")
sights = json_retreiver("Streets/sights.json")
sounds = json_retreiver("Streets/sounds.json")
smells = json_retreiver("Streets/smells.json")
use = json_retreiver("Streets/use.json")
infastructure_type = json_retreiver("Streets/infastructure_type.json")
details = json_retreiver("Streets/details.json")

if __name__ == "__main__":
    print_street()
