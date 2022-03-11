# ghosts.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random ghost."""


from random import choice as rc
from utils import json_retreiver


class Ghost(object):
    """A randomly generated ghost, the likes of which would haunt doskvol or
    the deathlands"""

    def __init__(self):
        self.first_name = rc(json_retreiver("../data/Ghosts/first_names.json"))
        self.family_name = rc(json_retreiver("../data/Ghosts/family_names.json"))
        self.alias = rc(json_retreiver("../data/Ghosts/aliases.json"))
        self.ghost_trait = rc(json_retreiver("../data/Ghosts/ghost_traits.json"))
        self.ghost_effect = rc(json_retreiver("../data/Ghosts/ghostly_effect.json"))

    def describe_ghost(self):
        """Returns a string that describes a ghost based on its attributes"""
        output = f"""
The ghost of {self.first_name.capitalize()} '{self.alias.capitalize()}' {self.family_name.capitalize()}.
There is/are (a/an) {self.ghost_effect.lower()} when this {self.ghost_trait.lower()} spirit appears!
    """
        return output


if __name__ == "__main__":
    g = Ghost()
    print(g.describe_ghost())
