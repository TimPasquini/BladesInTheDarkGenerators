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


def rc(variable):
    """rc = random choice. Picks a random item from the list and returns
    it. This is mostly to shorten up the variables in the print command"""
    return random.choice(variable)


def print_building(quality):
    """This prints a random description of a building, the "quality" argument
    needs to be "rare" or "common"""
    if quality == "rare":
        print(
            f"""
        This {rc(exterior_details)} {rc(material)} {rc(rare_use)} is notable
        for it's {rc(interior_details)} and {rc(interior_details)}"""
        )
    elif quality == "common":
        print(
            f"""
        This {rc(exterior_details)} {rc(material)} {rc(common_use)} is
        notable for it's {rc(interior_details)} and {rc(interior_details)}"""
        )
    else:
        print("Please enter 'rare' or 'common' as an argument")


common_use = json_retreiver("Buildings/common_use.json")
rare_use = json_retreiver("Buildings/rare_use.json")
material = json_retreiver("Buildings/material.json")
exterior_details = json_retreiver("Buildings/exterior_details.json")
interior_details = json_retreiver("Buildings/interior_details.json")


if __name__ == "__main__":
    chosen_building = sys.argv[1]
    print_building(chosen_building)
