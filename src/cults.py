# cults.py
"""The cults class creates a randomly generated cult instance utilizing
the rolling tables from the end of the Blades in the Dark rule book."""

from generator import Generator
from dataSets import CULT


class Cult(Generator):
    """A randomly generated Cult operating in the city of Doskvol.

    By default, all attributes are randomly created from the source lists. If
    a specific cult with specific attributes is needed, any attribute can
    be overridden with a string.

    ...

    Attributes
    ----------
    god: str or None
        What Forgotten God the cult follows
    practice: str or None
        The method in which the cult shows their devotion to their god

    Methods
    -------
    describe()
        Returns a formatted string describing the cult
    """

    def __init__(self, god=None, practice=None):
        self.god = self.simple_attribute_setter(god, CULT["FORGOTTEN_GODS"])
        self.practice = self.simple_attribute_setter(practice, CULT["PRACTICES"])

    def __str__(self):
        return f"a cult of {self.god}"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.god}', '{self.practice}')"

    def describe(self):
        """returns a string that describes a cult based on its attributes"""
        output = f"""
This is the cult of {self.god.title()}.
Their cultists follow an edict of:
    {self.practice.capitalize()}
        """
        return output


if __name__ == "__main__":
    c = Cult()
    print(c.describe())
