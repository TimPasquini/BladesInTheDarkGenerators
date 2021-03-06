# streets.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random streetscape."""

from utils import *
from dataSets import *


class Street(object):
    """A description of a randomly generated street in the city of Doskvol

    By default, all attributes are randomly created from the source lists. If
    a specific street with specific attributes is needed, any attribute can
    be overridden with a string.

    ...

    Attributes
    ----------
    mood: str or None
        The general ambiance of the street
    sight: str or None
        A defining visual feature of the street
    sound: str or None
        A defining audible feature of the street
    smell: str or None
        A defining aromatic feature of the street
    use: str or None
        What the street is generally used for, zoning purpose
    infastructure_type: str or None
        The type of street in terms of infastructure design (street, alley,
        waterway, plaza, etc)
    primary_detail: str or None
        An feature to make the street more interesting
    secondary_detail: str or None
        A second feature to make the street more interesting

    Methods
    -------
    describe()
        Returns a formatted string describing the street
    """

    def __init__(
        self,
        mood=None,
        sight=None,
        sound=None,
        smell=None,
        use=None,
        infastructure_type=None,
        primary_detail=None,
        secondary_detail=None,
    ):
        self.mood = simple_attribute_setter(mood, STREET_MOODS)
        self.sight = simple_attribute_setter(sight, STREET_SIGHTS)
        self.sound = simple_attribute_setter(sound, STREET_SOUNDS)
        self.smell = simple_attribute_setter(smell, STREET_SMELLS)
        self.use = simple_attribute_setter(use, STREET_USES)
        self.infastructure_type = simple_attribute_setter(
            infastructure_type, STREET_INFASTRUCTURE_TYPES
        )
        self.primary_detail = simple_attribute_setter(primary_detail, STREET_DETAILS)
        self.secondary_detail = simple_attribute_setter(secondary_detail, STREET_DETAILS)

    def __str__(self):
        return f"a {self.infastructure_type} used for {self.use}"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.mood}', '{self.sight}', '{self.sound}', '{self.smell}', '{self.use}', '{self.infastructure_type}', '{self.primary_detail}', '{self.secondary_detail}')"

    def describe(self):
        """returns a string describing a street using its attributes"""
        output = f"""
This {self.mood} {self.infastructure_type} is primarily used for {self.use} purposes.
(A/An) {self.sight} catch(es) your eye.
You hear {self.sound} and smell {self.smell} on the air.
You can't help but notice {self.primary_detail} and {self.secondary_detail}."""
        return output


if __name__ == "__main__":
    s = Street()
    print(s.describe())
