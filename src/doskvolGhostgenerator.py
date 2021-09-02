# doskvolGhostGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random ghost.

from utils import rc, json_retreiver


def print_ghost(ghost_dict):
    """This will print text that describes a new ghost"""
    output = f"""
This is the ghost of {ghost_dict["first_name"].capitalize()} '{ghost_dict["aliases"].capitalize()}' {ghost_dict["family_name"].capitalize()}.
There is/are (a/an) {ghost_dict["ghostly_effect"].lower()} when this {ghost_dict["ghost_trait"].lower()} spirit appears!
    """
    print(output)
    return output


def build_ghost():
    """Call the function by assigning to a variable that gets passed to
    print_ghost(). This function pulls lists from the .json files and then
    selects a random entry from that, then assigns to a dict. You need to
    re-call this function if you want a new set of random variables."""
    ghost_dict = {}
    ghost_dict["first_name"] = rc(json_retreiver("Ghosts/first_names.json"))
    ghost_dict["family_name"] = rc(json_retreiver("Ghosts/family_names.json"))
    ghost_dict["aliases"] = rc(json_retreiver("Ghosts/aliases.json"))
    ghost_dict["ghost_trait"] = rc(json_retreiver("Ghosts/ghost_traits.json"))
    ghost_dict["ghostly_effect"] = rc(json_retreiver("Ghosts/ghostly_effect.json"))
    return ghost_dict


if __name__ == "__main__":
    random_ghost = build_ghost()
    print_ghost(random_ghost)
