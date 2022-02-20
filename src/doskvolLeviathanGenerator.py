# doskvolLeviathanGenerator.py
# Uses the tables in the Leviathan Song supplement to generate a description
# for a leviathan and it's spawn. Use an argument of "surreal" or "banal"
# in the terminal to determine the leviathan's activity when spotted

import sys
import random
from random import choice as rc

from utils import json_retreiver


def print_leviathan(quality, leviathan_dict):
    """This will print a randomly generated Leviathan. Requires quality of
    either 'banal' or 'surreal' to decide the leviathan's activity upon arrival"""
    if quality == "banal":
        activity = leviathan_dict["banal"]
    elif quality == "surreal":
        activity = leviathan_dict["surreal"]
    else:
        print("Please enter 'surreal' or 'banal' as an argument.")
        return
    intro = f"A leviathan is {activity.lower()} before you in the water. It is none other than {leviathan_dict['name'].capitalize()}, '{leviathan_dict['epithet'].title()}.' "
    form = f"This leviathan has the head of a {leviathan_dict['shape_1']}, the body of a {leviathan_dict['shape_2']} and moves on the limbs of a {leviathan_dict['shape_3']}. "
    size = f"There are {leviathan_dict['size']} distinct regions on this leviathan's body:\n"
    spawn = f"This leviathan is known to spawn (a/an) {leviathan_dict['spawn']}."
    # Create a list of region descriptions for every region in the leviathan
    region_list = []
    for num in range(1, (leviathan_dict["size"] + 1)):
        active_region = leviathan_dict[f"region_{num}"]
        region_description = f"Region {num} is notable for its {active_region}.\n"
        region_list.append(region_description)
    # TODO: iterative process for displaying treasures
    treasure_list = ["Braving the regions could lead to valuable treasure:\n"]
    for num in range(1, (leviathan_dict["treasure_index"] + 1)):
        active_treasure = leviathan_dict[f"treasure_{num}"]
        treasure_description = f"{active_treasure}.\n"
        treasure_list.append(treasure_description)
    # concatenate string peices and return it
    output_string = (
        intro + form + size + "".join(region_list) + "".join(treasure_list) + spawn
    )
    return output_string


def print_spawn():
    """call this function when you want to generate a new or additional spawn
    from the leviathan"""
    output = f"The leviathan releases new spawn, it emits (a/an) {spawner().lower()}"
    return output


def spawner():
    """The spawner will select a spawn from the spawn.json and check if it is
    one of the variable type spawns it will generate a spawn from the appropriate
    criteria. Spawner can be called independently but will only return the
    actual spawn. Use the print_spawn() function to get flavor text."""
    spawn = rc(json_retreiver("Leviathan/leviathan_spawn.json"))
    if spawn == "trigger three shapes":
        spawn = f"hybrid of a {_grab_shape()}, a {_grab_shape()}, and a {_grab_shape()}"
    elif spawn == "trigger shape humanoid":
        spawn = f"humanoid {_grab_shape()}"
    elif spawn == "trigger shape inside-out":
        spawn = f"{_grab_shape()} turned inside-out"
    elif spawn == "trigger shape flying":
        spawn = f"flying {_grab_shape()}"
    elif spawn == "trigger ghosts":
        intro = "multitude of ghosts. There is/are (a/an) "
        outro = "dead sailors and other spectral eminations appear"
        spawn = intro + str(_grab_ghost()) + outro
    elif spawn == "trigger demon":
        spawn = str(_grab_demon())
    return spawn


def _grab_shape():
    """grabs from the shape-list, used to build_leviathan() and for spawner()"""
    return rc(json_retreiver("Leviathan/shapes.json"))


def _grab_ghost():
    """constructs a ghost trait and effect for the spawner and returns a string"""
    trait = rc(json_retreiver("Ghosts/ghost_traits.json"))
    effect = rc(json_retreiver("Ghosts/ghostly_effect.json"))
    return f"{effect.lower()} when these {trait.lower()} "


def _grab_demon():
    """constructs a simple demon and returns a string"""
    feature = rc(json_retreiver("Demons/demon_features.json"))
    aspect = rc(json_retreiver("Demons/demonic_aspect.json"))
    affinity = rc(json_retreiver("Demons/demonic_affinity.json"))
    demon = f"{aspect.lower()} {affinity.lower()} demon with {feature.lower()}"
    return demon


def build_leviathan():
    """Based on the generation criteria laid out by Leviathan Song, a leviathan
    needs a name or epithet, 2-3 shapes, a size expressed a number representing
    distinct "areas" on the leviathan, each area gets a demon trait, some
    percentage of areas should have a treasure, and each leviathan should have
    a spawn. For now, all leviathans will have 3 shapes and 25% of areas with
    have treasure with a minimum of 1."""
    leviathan_dict = {}
    leviathan_dict["banal"] = rc(json_retreiver("Leviathan/banal_activity.json"))
    leviathan_dict["surreal"] = rc(json_retreiver("Leviathan/surreal_activity.json"))
    leviathan_dict["name"] = rc(json_retreiver("Leviathan/leviathan_names.json"))
    leviathan_dict["epithet"] = rc(json_retreiver("Leviathan/epithet.json"))
    leviathan_dict["shape_1"] = _grab_shape()
    leviathan_dict["shape_2"] = _grab_shape()
    leviathan_dict["shape_3"] = _grab_shape()
    leviathan_dict["size"] = random.randint(1, 6) + 4
    # use the size value to generate demon traits for each region
    for num in range(1, (leviathan_dict["size"] + 1)):
        leviathan_dict[f"region_{num}"] = rc(
            json_retreiver("Leviathan/leviathan_demon_traits.json")
        )
    # generate treasures for leviathan
    leviathan_dict["treasure_index"] = round((leviathan_dict["size"] / 4) + 1)
    for num in range(1, (leviathan_dict["treasure_index"] + 1)):
        leviathan_dict[f"treasure_{num}"] = rc(
            json_retreiver("Leviathan/leviathan_treasures.json")
        )
    leviathan_dict["spawn"] = spawner()
    return leviathan_dict


if __name__ == "__main__":
    chosen_activity = sys.argv[1]
    leviathan_dict = build_leviathan()
    print(print_leviathan(chosen_activity, leviathan_dict))
