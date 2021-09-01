# doskvolBuildingGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random building. Use an argument of "rare" or "common" in the terminal

import sys

from utils import rc, json_retreiver


def print_building(quality, building_dict):
    """This prints a random description of a building, the "quality" argument
    needs to be "rare" or "common"""
    if quality == "rare":
        output = f"""
        This {building_dict["material"].lower()} {building_dict["rare_use"].lower()} building is decorated with {building_dict["exterior_details"].lower()}.
        It is notable for it's {building_dict["interior_details_1"].lower()} and {building_dict["interior_details_2"].lower()}"""
        print(output)
        return output
    elif quality == "common":
        output = f"""
        This {building_dict["material"].lower()} {building_dict["common_use"].lower()} building is decorated with {building_dict["exterior_details"].lower()}.
        It is notable for it's {building_dict["interior_details_1"].lower()} and {building_dict["interior_details_2"].lower()}"""
        print(output)
        return output
    else:
        print("Please enter 'rare' or 'common' as an argument")


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
    chosen_building = sys.argv[1]
    print_building(chosen_building)
