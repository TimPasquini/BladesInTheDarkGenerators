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


def rc(variable):
    """rc = random choice. Picks a random item from the list and returns
    it. This is mostly to shorten up the variables in the print command"""
    return random.choice(variable)


def print_person(quality):
    """This prints a random description of a person, the "quality" argument
    needs to be "rare" or "common"""
    if quality == "rare":
        output = f"""
        {rc(first_name)} '{rc(aliases)}' {rc(family_name)}:
        A/An {rc(appearance)} {rc(gender)} {random.choices(heritage, weights=[50, 10, 5, 5, 5, 5])[0]} wearing/using a/an {rc(style)}.
        They work as a {rc(rare_profession)} and use {rc(methods)} to try and gain/cause {rc(goals)}.
        Overall, they seem {rc(traits)} but are also {rc(quirks)} They are interested in {rc(interests)}.
        """
        print(output)
        return output

    elif quality == "common":
        output = f"""
        {rc(first_name)} '{rc(aliases)}' {rc(family_name)}:
        A {rc(appearance)} {rc(gender)} {random.choices(heritage, weights=[50, 10, 5, 5, 5, 5])[0]} wearing/using a/an {rc(style)}.
        They work as a {rc(common_profession)} and use {rc(methods)} to try and gain/cause {rc(goals)}.
        Overall, they seem {rc(traits)} but are also {rc(quirks)} They are interested in {rc(interests)}.
        """
        print(output)
        return output
    else:
        print("Please enter 'rare' or 'common' as an argument")


heritage = json_retreiver("People/heritage.json")
gender = json_retreiver("People/gender.json")
appearance = json_retreiver("People/appearance.json")
goals = json_retreiver("People/goals.json")
methods = json_retreiver("People/methods.json")
common_profession = json_retreiver("People/common_profession.json")
rare_profession = json_retreiver("People/rare_profession.json")
style = json_retreiver("People/style.json")
traits = json_retreiver("People/traits.json")
interests = json_retreiver("People/interests.json")
quirks = json_retreiver("People/quirks.json")

first_name = json_retreiver("People/first_names.json")
family_name = json_retreiver("People/family_names.json")
aliases = json_retreiver("People/aliases.json")


if __name__ == "__main__":
    chosen_person = sys.argv[1]
    print_person(chosen_person)
