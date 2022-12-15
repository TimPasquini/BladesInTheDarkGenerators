# ghosts.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random ghost."""

from generator import Generator
from dataSets import GHOST, PEOPLE


class Ghost(Generator):
    """A randomly generated ghost, the likes of which would haunt doskvol or
    the deathlands

    By default, all attributes are randomly created from the source lists. If
    a specific ghost with specific attributes is needed, any attribute can
    be overridden with a string.

    ...

    Attributes
    ----------
    first_name: str or None
        The given name the ghost had in life
    family_name: str or None
        The surname the ghost had in life
    alias: str or None
        The alias the ghost used in life
    ghost_trait: str or None
        The primary personality trait of the ghost
    ghost_effect: str or None
        A strange effect that occurs around the ghost when it manifests

    Methods
    -------
    describe()
        Returns a formatted string describing the ghost
    """

    def __init__(
        self,
        first_name=None,
        family_name=None,
        alias=None,
        ghost_trait=None,
        ghost_effect=None,
    ):
        self.first_name = self.simple_attribute_setter(first_name, PEOPLE["FIRST_NAMES"])
        self.family_name = self.simple_attribute_setter(family_name, PEOPLE["FAMILY_NAMES"])
        self.alias = self.simple_attribute_setter(alias, PEOPLE["ALIASES"])
        self.ghost_trait = self.simple_attribute_setter(ghost_trait, GHOST["TRAITS"])
        self.ghost_effect = self.simple_attribute_setter(ghost_effect, GHOST["EFFECTS"])

    def __str__(self):
        return f"{self.first_name} '{self.alias}' {self.family_name}, a ghost"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.first_name}', '{self.family_name}', '{self.alias}', '{self.ghost_trait}', '{self.ghost_effect}')"

    def describe(self):
        """Returns a string that describes a ghost based on its attributes"""
        output = f"""
The ghost of {self.first_name.capitalize()} '{self.alias.capitalize()}' {self.family_name.capitalize()}.
There is {self.ghost_effect} when this {self.ghost_trait} spirit appears!
    """
        return output


if __name__ == "__main__":
    g = Ghost()
    print(g.describe())
