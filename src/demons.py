# demons.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random demon."""

from utils import *


class Demon(object):
    """A randomly generated demon, the likes of which would haunt doskvol or the
    deathlands"""

    def __init__(
        self,
        name=None,
        primary_feature=None,
        secondary_feature=None,
        aspect=None,
        affinity=None,
        desire=None,
    ):
        self.name = simple_attribute_setter(name, "Demons/demon_names.json")
        self.primary_feature = simple_attribute_setter(
            primary_feature, "Demons/demon_features.json"
        )
        self.secondary_feature = simple_attribute_setter(
            secondary_feature, "Demons/demon_features.json"
        )
        self.aspect = simple_attribute_setter(aspect, "Demons/demonic_aspect.json")
        self.affinity = simple_attribute_setter(
            affinity, "Demons/demonic_affinity.json"
        )
        self.desire = simple_attribute_setter(desire, "Demons/demon_desire.json")

    def __str__(self):
        return f"{self.name}, a {self.aspect} {self.affinity} demon"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.name}', '{self.primary_feature}', '{self.secondary_feature}', '{self.aspect}', '{self.affinity}', '{self.desire}')"

    def describe(self):
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
    print(d.describe())
