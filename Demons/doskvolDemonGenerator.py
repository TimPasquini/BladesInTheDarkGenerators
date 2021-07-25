# doskvolDemonGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random demon.

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


def print_demon():
    """This will print text describing a new demon"""
    print(
        f"""
    Tremble at the sight of {rc(demon_name)}!
    Behold, {rc(demon_features)} and {rc(demon_features)}.
    This {rc(demonic_affinity)} demon has a {rc(demonic_aspect)} aspect.
    This demon desires {rc(demon_desire)} above all else!
    """
    )


demon_name = json_retreiver("demon_names.json")
demon_features = json_retreiver("demon_features.json")
demonic_aspect = json_retreiver("demonic_aspect.json")
demonic_affinity = json_retreiver("demonic_affinity.json")
demon_desire = json_retreiver("demon_desire.json")

if __name__ == "__main__":
    print_demon()
