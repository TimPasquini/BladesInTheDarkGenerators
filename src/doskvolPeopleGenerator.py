# doskvolPeopleGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random person. Use an argument of "rare" or "common" in the terminal

import sys
import random

from utils import rc, json_retreiver


def print_person(quality, person_dict):
    """This prints a random description of a person, the "quality" argument
    needs to be "rare" or "common"""
    if quality == "rare":
        output = f"""
        {person_dict["first_name"]} '{person_dict["aliases"]}' {person_dict["family_name"]}:
        A/An {person_dict["appearance"]} {person_dict["gender"]} {person_dict["heritage"]} wearing/using a/an {person_dict["style"]}.
        They work as a {person_dict["rare_profession"]} and use {person_dict["methods"]} to try and gain/cause {person_dict["goals"]}.
        Overall, they seem {person_dict["traits"]} but are also {person_dict["quirks"]} They are interested in {person_dict["interests"]}.
        """
        print(output)
        return output
    elif quality == "common":
        output = f"""
        {person_dict["first_name"]} '{person_dict["aliases"]}' {person_dict["family_name"]}:
        A {person_dict["appearance"]} {person_dict["gender"]} {person_dict["heritage"]} wearing/using a/an {person_dict["style"]}.
        They work as a {person_dict["common_profession"]} and use {person_dict["methods"]} to try and gain/cause {person_dict["goals"]}.
        Overall, they seem {person_dict["traits"]} but are also {person_dict["quirks"]} They are interested in {person_dict["interests"]}.
        """
        print(output)
        return output
    else:
        print("Please enter 'rare' or 'common' as an argument")


def build_person():
    """Call the function by assigning to a variable that gets passed to
    print_person(). This function pulls lists from the .json files and then
    selects a random entry from that, then assigns to a dict. You need to
    re-call this function if you want a new set of random variables."""
    person_dict = {}
    person_dict["heritage"] = random.choices(json_retreiver("People/heritage.json"), weights=[50, 10, 5, 5, 5, 5])[0]
    person_dict["gender"] = rc(json_retreiver("People/gender.json"))
    person_dict["appearance"] = rc(json_retreiver("People/appearance.json"))
    person_dict["goals"] = rc(json_retreiver("People/goals.json"))
    person_dict["methods"] = rc(json_retreiver("People/methods.json"))
    person_dict["common_profession"] = rc(json_retreiver("People/common_profession.json"))
    person_dict["rare_profession"] = rc(json_retreiver("People/rare_profession.json"))
    person_dict["style"] = rc(json_retreiver("People/style.json"))
    person_dict["traits"] = rc(json_retreiver("People/traits.json"))
    person_dict["interests"] = rc(json_retreiver("People/interests.json"))
    person_dict["quirks"] = rc(json_retreiver("People/quirks.json"))
    person_dict["first_name"] = rc(json_retreiver("People/first_names.json"))
    person_dict["family_name"] = rc(json_retreiver("People/family_names.json"))
    person_dict["aliases"] = rc(json_retreiver("People/aliases.json"))
    return person_dict


if __name__ == "__main__":
    chosen_person = sys.argv[1]
    print_person(chosen_person)
