# streets.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random streetscape."""


from random import choice as rc
from utils import json_retreiver


class Street(object):
    """A description of a randomly generated street in the city of Doskvol"""

    def __init__(self):
        self.mood = rc(json_retreiver("Streets/moods.json"))
        self.sight = rc(json_retreiver("Streets/sights.json"))
        self.sound = rc(json_retreiver("Streets/sounds.json"))
        self.smell = rc(json_retreiver("Streets/smells.json"))
        self.use = rc(json_retreiver("Streets/use.json"))
        self.infastructure_type = rc(json_retreiver("Streets/infastructure_type.json"))
        self.primary_detail = rc(json_retreiver("Streets/details.json"))
        self.secondary_detail = rc(json_retreiver("Streets/details.json"))

    def describe_street(self):
        """returns a string describing a street using its attributes"""
        output = f"""
This {self.mood} {self.infastructure_type} is primarily used for {self.use} purposes.
(A/An) {self.sight} catch(es) your eye.
You hear {self.sound} and smell {self.smell} on the air.
You can't help but notice {self.primary_detail} and {self.secondary_detail}."""
        return output


if __name__ == "__main__":
    s = Street()
    print(s.describe_street())
