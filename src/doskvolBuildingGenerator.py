# doskvolBuildingGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random building. Use an argument of "rare" or "common" in the terminal

import sys
from random import choice as rc

from utils import json_retreiver


def print_building(quality, building_dict):
    """This prints a random description of a building, the "quality" argument
    needs to be "rare" or "common"""
    rare = building_dict['rare_use'].lower()
    common = building_dict['common_use'].lower()
    if quality == "rare":
        building_kind = rare
    elif quality == "common":
        building_kind = common
    elif quality == "both":
        building_kind = f"{common}/{rare}"
    else:
        print("Please enter 'rare', 'common', or 'both' as an argument")
        return
    output = (f"This {building_dict['material'].lower()} {building_kind} "
              f"building is decorated with {building_dict['exterior_details'].lower()}.\n"
              f"It is notable for it's {building_dict['interior_details_1'].lower()} "
              f"and {building_dict['interior_details_2'].lower()}")
    return output


def build_building():
    """Call the function by assigning to a variable that gets passed to
    print_building(). This function pulls lists from the .json files and then
    selects a random entry from that, then assigns to a dict. You need to
    re-call this function if you want a new set of random variables."""
    building_dict = {}
    building_dict["common_use"] = rc(json_retreiver("Buildings/common_use.json"))
    building_dict["rare_use"] = rc(json_retreiver("Buildings/rare_use.json"))
    building_dict["material"] = rc(json_retreiver("Buildings/material.json"))
    building_dict["exterior_details"] = rc(
        json_retreiver("Buildings/exterior_details.json")
    )
    building_dict["interior_details_1"] = rc(
        json_retreiver("Buildings/interior_details.json")
    )
    building_dict["interior_details_2"] = rc(
        json_retreiver("Buildings/interior_details.json")
    )
    return building_dict


if __name__ == "__main__":
    try:
        chosen_building = sys.argv[1]
    except IndexError:  # no building type specified
        chosen_building = "both"
    b = build_building()
    print(print_building(chosen_building, b))
