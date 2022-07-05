# ghosts.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random ghost."""

from utils import *


class Ghost(object):
    """A randomly generated ghost, the likes of which would haunt doskvol or
    the deathlands"""

    def __init__(
        self,
        first_name=None,
        family_name=None,
        alias=None,
        ghost_trait=None,
        ghost_effect=None,
    ):
        self.first_name = simple_attribute_setter(first_name, "People/first_names.json")
        self.family_name = simple_attribute_setter(
            family_name, "People/family_names.json"
        )
        self.alias = simple_attribute_setter(alias, "People/aliases.json")
        self.ghost_trait = simple_attribute_setter(
            ghost_trait, "Ghosts/ghost_traits.json"
        )
        self.ghost_effect = simple_attribute_setter(
            ghost_effect, "Ghosts/ghostly_effect.json"
        )

    def __str__(self):
        return f"{self.first_name} '{self.alias}' {self.family_name}, a ghost"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.first_name}', '{self.family_name}', '{self.alias}', '{self.ghost_trait}', '{self.ghost_effect}')"

    def describe(self):
        """Returns a string that describes a ghost based on its attributes"""
        output = f"""
The ghost of {self.first_name.capitalize()} '{self.alias.capitalize()}' {self.family_name.capitalize()}.
There is/are (a/an) {self.ghost_effect.lower()} when this {self.ghost_trait.lower()} spirit appears!
    """
        return output


if __name__ == "__main__":
    g = Ghost()
    print(g.describe())
