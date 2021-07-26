# doskvolGhostGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random ghost.

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


def print_ghost():
    """This will print text that describes a new ghost"""
    output = f"""
    This is the ghost of {rc(first_name)} '{rc(aliases)}' {rc(family_name)}.
    There is/are (a/an) {rc(ghostly_effect)} when this {rc(ghost_trait)} spirit appears!
    """
    print(output)
    return output


first_name = json_retreiver("Ghosts/first_names.json")
family_name = json_retreiver("Ghosts/family_names.json")
aliases = json_retreiver("Ghosts/aliases.json")
ghost_trait = json_retreiver("Ghosts/ghost_traits.json")
ghostly_effect = json_retreiver("Ghosts/ghostly_effect.json")

if __name__ == "__main__":
    print_ghost()
