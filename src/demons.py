# demons.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random demon."""

from generator import Generator
from dataSets import DEMON


class Demon(Generator):
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
        name: str | None = None,
        primary_feature: str | None = None,
        secondary_feature: str | None = None,
        aspect: str | None = None,
        affinity: str | None = None,
        desire: str | None = None,
    ):
        self.name = self.simple_attribute_setter(name, DEMON["NAMES"])
        self.primary_feature = self.simple_attribute_setter(
            primary_feature, DEMON["FEATURES"]
        )
        # use secondary roll check to ensure we get something different
        self.secondary_feature = secondary_feature
        self.aspect = self.simple_attribute_setter(aspect, DEMON["ASPECTS"])
        self.affinity = self.simple_attribute_setter(affinity, DEMON["AFFINITIES"])
        self.desire = self.simple_attribute_setter(desire, DEMON["DESIRES"])

    def __str__(self):
        return f"{self.name}, a {self.aspect} {self.affinity} demon"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.name}', '{self.primary_feature}', '{self.secondary_feature}', '{self.aspect}', '{self.affinity}', '{self.desire}')"

    @property
    def secondary_feature(self):
        return self._secondary_feature

    @secondary_feature.setter
    def secondary_feature(self, detail: str | None):
        # check if None and roll something if it is
        initial_detail = self.simple_attribute_setter(detail, DEMON["FEATURES"])

        # use second_roll_check to ensure it's different from the primary feature
        self._secondary_feature = self.second_roll_check(
            initial_detail,
            [self.primary_feature],  # make the primary a trigger
            [self.primary_feature],  # make the primary forbidden
            DEMON["FEATURES"],
        )

    def describe(self) -> str:
        """Returns a description of the demon based on its attributes"""
        output = f"""
Tremble at the sight of {self.name.capitalize()}!
Behold, its {self.primary_feature} and {self.secondary_feature}.
This {self.affinity} demon has a {self.aspect} aspect.
This demon desires {self.desire} above all else!
        """
        return output


if __name__ == "__main__":
    d = Demon()
    print(d.describe())
