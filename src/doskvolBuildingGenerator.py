# doskvolBuildingGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random building. Use an argument of "rare" or "common" in the terminal

import sys

from utils import rc, json_retreiver


def print_building(quality):
    """This prints a random description of a building, the "quality" argument
    needs to be "rare" or "common"""
    if quality == "rare":
        output = f"""
        This {rc(material)} {rc(rare_use)} building is decorated with {rc(exterior_details)}.
        It is notable for it's {rc(interior_details)} and {rc(interior_details)}"""
        print(output)
        return output
    elif quality == "common":
        output = f"""
        This {rc(material)} {rc(common_use)} building is decorated with {rc(exterior_details)}.
        It is notable for it's {rc(interior_details)} and {rc(interior_details)}"""
        print(output)
        return output
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
