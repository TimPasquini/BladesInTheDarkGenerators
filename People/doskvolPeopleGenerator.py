# doskvolPeopleGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random person. Use an argument of "rare" or "common" in the terminal

import random
import json
import sys


def json_retreiver(json_filename):
    """Call this from a variable with a filename string to populate
    with json content"""
    filename = json_filename
    with open(filename) as f:
        return json.load(f)


heritage = json_retreiver("heritage.json")
gender = json_retreiver("gender.json")
appearance = json_retreiver("appearance.json")
goals = json_retreiver("goals.json")
methods = json_retreiver("methods.json")
common_profession = json_retreiver("common_profession.json")
rare_profession = json_retreiver("rare_profession.json")
style = json_retreiver("style.json")
traits = json_retreiver("traits.json")
interests = json_retreiver("interests.json")
quirks = json_retreiver("quirks.json")

first_name = json_retreiver("first_names.json")
family_name = json_retreiver("family_names.json")
aliases = json_retreiver("aliases.json")

chosen_person = sys.argv[1]

if chosen_person == "rare":
    print(
        f"""
        {random.choice(first_name)} '{random.choice(aliases)}' {random.choice(family_name)}.
        A/An {random.choice(appearance)} {random.choice(gender)} {random.choices(heritage, weights=[50, 10, 5, 5, 5, 5])[0]} wearing/using a/an {random.choice(style)}.
        They work as a {random.choice(rare_profession)} and use {random.choice(methods)} to try and gain/cause {random.choice(goals)}.
        Overall, they seem {random.choice(traits)} but are also {random.choice(quirks)} They are interested in {random.choice(interests)}.
        """
    )
elif chosen_person == "common":
    print(
        f"""
        {random.choice(first_name)} '{random.choice(aliases)}' {random.choice(family_name)}.
        A {random.choice(appearance)} {random.choice(gender)} {random.choices(heritage, weights=[50, 10, 5, 5, 5, 5])[0]} wearing/using a/an {random.choice(style)}.
        They work as a {random.choice(common_profession)} and use {random.choice(methods)} to try and gain/cause {random.choice(goals)}.
        Overall, they seem {random.choice(traits)} but are also {random.choice(quirks)} They are interested in {random.choice(interests)}.
        """
    )
else:
    print("Please enter 'rare' or 'common' as an argument")
