# demons.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random demon."""

from utils import *
from dataSets import *


class Demon(object):
    """A randomly generated demon, the likes of which would haunt doskvol or the
    deathlands.

    By default, all attributes are randomly created from the source lists. If
    a specific demon with specific attributes is needed, any attribute can
    be overridden with a string.

    ...

    Attributes
    ----------
    name: str or None
        The name the demon goes by
    primary_feature: str or None
        All demons have features that make it clear they are not human
    secondary_feature: str or None
        All demons have features that make it clear they are not human
    aspect: str or None
        The physical way in which a demon manifests itself
    affinity: str or None
        The primal force or element the demon is connected to
    desire: str or None
        Demons are the embodiment of a dark obsession

    Methods
    -------
    describe()
        Returns a formatted string describing the demon
    """

    def __init__(
        self,
        name=None,
        primary_feature=None,
        secondary_feature=None,
        aspect=None,
        affinity=None,
        desire=None,
    ):
        self.name = simple_attribute_setter(name, DEMON_NAMES)
        self.primary_feature = simple_attribute_setter(primary_feature, DEMON_FEATURES)
        self.secondary_feature = simple_attribute_setter(
            secondary_feature, DEMON_FEATURES
        )
        self.aspect = simple_attribute_setter(aspect, DEMON_ASPECTS)
        self.affinity = simple_attribute_setter(affinity, DEMON_AFFINITIES)
        self.desire = simple_attribute_setter(desire, DEMON_DESIRES)

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
