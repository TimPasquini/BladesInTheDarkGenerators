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


demon_name = json_retreiver('demon_names.json')
demon_features = json_retreiver('demon_features.json')
demonic_aspect = json_retreiver('demonic_aspect.json')
demonic_affinity = json_retreiver('demonic_affinity.json')
demon_desire = json_retreiver('demon_desire.json')

print(
    f"""
    Tremble at the sight of {random.choice(demon_name)}!
    Behold their {random.choice(demon_features)} and {random.choice(demon_features)}.
    This {random.choice(demonic_affinity)} demon has a {random.choice(demonic_aspect)} aspect.
    This demon desires {random.choice(demon_desire)} above all else!
    """)