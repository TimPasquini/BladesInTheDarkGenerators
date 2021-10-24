# doskvolPeopleGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random person. Use an argument of "rare" or "common" in the terminal

import sys
import random
from random import choice as rc

from utils import json_retreiver


def print_person(quality, person_dict):
    """This prints a random description of a person, the "quality" argument
    needs to be "rare" or "common"""
    person_dict = _tycherosi_heritage_check(person_dict)
    name = (f"{person_dict['first_name'].capitalize()} "
            f"'{person_dict['aliases'].capitalize()}' "
            f"{person_dict['family_name'].capitalize()}:\n")
    heritage = (f"A/An {person_dict['appearance'].lower()} " 
                f"{person_dict['gender'].lower()} "
                f"{person_dict['heritage'].capitalize()} "
                f"wearing/using a/an {person_dict['style'].lower()}.\n")
    quirk = (f"Overall, they seem {person_dict['traits'].lower()} "
             f"but are also {person_dict['quirks'].lower()}.\n" 
             f"They are interested in {person_dict['interests'].lower()}.\n")

    common_profession = person_dict['common_profession']
    rare_profession = person_dict['rare_profession']
    if quality == "common":
        profession_t = common_profession
    elif quality == "rare":
        profession_t = rare_profession
    elif quality == "both":
        profession_t = f"{common_profession}/{rare_profession}"
    else:
        print("Please enter 'rare', 'common', or 'both' as an argument.")
        return

    profession = (f"They work as a {profession_t} and use "
                  f"{person_dict['methods'].lower()} to try and "
                  f"gain/cause {person_dict['goals'].lower()}.\n")  # TODO: Dynamic gain/cause

    if "demonic" in person_dict:
        demonic_trait = (f"Their Tycherosi heritage manifests as "  # TODO: Dynamic a/an
                         f"(a/an) {person_dict['demonic'].lower()}.\n")
        output = name + heritage + demonic_trait + profession + quirk
    else:
        output = name + heritage + profession + quirk
    return output


def _tycherosi_heritage_check(person_dict):
    """Tycherosi have tend to have a characteristic that makes them stand out
    due to the demonic blood in their veins, this function will check
    if for the heritage and add a demonic trait from the demon generator"""
    if person_dict["heritage"].lower() == "tycherosi":
        person_dict["demonic"] = rc(json_retreiver("Demons/demon_features.json"))
        return person_dict
    else:
        return person_dict


def build_person():
    """Call the function by assigning to a variable that gets passed to
    print_person(). This function pulls lists from the .json files and then
    selects a random entry from that, then assigns to a dict. You need to
    re-call this function if you want a new set of random variables."""
    person_dict = {}
    person_dict["heritage"] = random.choices(
        json_retreiver("People/heritage.json"), weights=[50, 10, 5, 5, 5, 5]
    )[0]
    person_dict["gender"] = rc(json_retreiver("People/gender.json"))
    person_dict["appearance"] = rc(json_retreiver("People/appearance.json"))
    person_dict["goals"] = rc(json_retreiver("People/goals.json"))
    person_dict["methods"] = rc(json_retreiver("People/methods.json"))
    person_dict["common_profession"] = rc(
        json_retreiver("People/common_profession.json")
    )
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
    try:
        chosen_person = sys.argv[1]
    except IndexError:
        chosen_person = 'both'
    person_dict = build_person()
    print(print_person(chosen_person, person_dict))
