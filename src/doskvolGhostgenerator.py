# doskvolGhostGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random ghost.

from utils import rc, json_retreiver


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
