# demons.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random demon."""

from random import choice as rc
from utils import json_retreiver


class Demon(object):
    """A randomly generated demon, the likes of which would haunt doskvol or the
    deathlands"""

    def __init__(self):
        self.name = rc(json_retreiver("Demons/demon_names.json"))
        self.primary_feature = rc(json_retreiver("Demons/demon_features.json"))
        self.secondary_feature = rc(json_retreiver("Demons/demon_features.json"))
        self.aspect = rc(json_retreiver("Demons/demonic_aspect.json"))
        self.affinity = rc(json_retreiver("Demons/demonic_affinity.json"))
        self.desire = rc(json_retreiver("Demons/demon_desire.json"))

    def describe_demon(self):
        """Returns a description of the demon based on its attributes"""
        output = f"""
Tremble at the sight of {self.name.capitalize()}!
Behold, {self.primary_feature.lower()} and {self.secondary_feature.lower()}.
This {self.affinity.lower()} demon has a {self.aspect.lower()} aspect.
This demon desires {self.desire.lower()} above all else!
        """
        return output


if __name__ == "__main__":
    d = Demon()
    print(d.describe_demon())
