# streets.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random streetscape."""

from generator import Generator
from dataSets import STREET


class Street(Generator):
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
    infrastructure_type: str or None
        The type of street in terms of infrastructure design (street, alley,
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
        infrastructure_type=None,
        primary_detail=None,
        secondary_detail=None,
    ):
        self.mood = self.simple_attribute_setter(mood, STREET["MOODS"])
        self.sight = self.simple_attribute_setter(sight, STREET["SIGHTS"])
        self.sound = self.simple_attribute_setter(sound, STREET["SOUNDS"])
        self.smell = self.simple_attribute_setter(smell, STREET["SMELLS"])
        self.use = self.simple_attribute_setter(use, STREET["USES"])
        self.infrastructure_type = Street.simple_attribute_setter(
            infrastructure_type, STREET["INFRASTRUCTURE_TYPES"]
        )
        self.primary_detail = self.simple_attribute_setter(primary_detail, STREET["DETAILS"])
        self.secondary_detail = self.simple_attribute_setter(
            secondary_detail, STREET["DETAILS"]
        )

    def __str__(self):
        return f"a {self.infrastructure_type} used for {self.use}"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.mood}', '{self.sight}', '{self.sound}', '{self.smell}', '{self.use}', '{self.infrastructure_type}', '{self.primary_detail}', '{self.secondary_detail}')"

    def describe(self):
        """returns a string describing a street using its attributes"""
        output = f"""
This {self.mood} {self.infrastructure_type} is primarily used for {self.use} purposes.
{self.sight.capitalize()} catches your eye.
You hear {self.sound} and smell {self.smell} on the air.
You can't help but notice {self.primary_detail} and {self.secondary_detail}."""
        return output


if __name__ == "__main__":
    s = Street()
    print(s.describe())
