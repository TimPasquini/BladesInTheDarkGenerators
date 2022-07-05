# streets.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random streetscape."""

from utils import *


class Street(object):
    """A description of a randomly generated street in the city of Doskvol"""

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
        self.mood = simple_attribute_setter(mood, "Streets/moods.json")
        self.sight = simple_attribute_setter(sight, "Streets/sights.json")
        self.sound = simple_attribute_setter(sound, "Streets/sounds.json")
        self.smell = simple_attribute_setter(smell, "Streets/smells.json")
        self.use = simple_attribute_setter(use, "Streets/use.json")
        self.infastructure_type = simple_attribute_setter(
            infastructure_type, "Streets/infastructure_type.json"
        )
        self.primary_detail = simple_attribute_setter(
            primary_detail, "Streets/details.json"
        )
        self.secondary_detail = simple_attribute_setter(
            secondary_detail, "Streets/details.json"
        )

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
