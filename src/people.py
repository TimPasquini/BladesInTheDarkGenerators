# people.py
"""The people class creates a randomly generated person utilizing
the rolling tables from the end of the Blades in the Dark rule book."""

import sys
from random import choice as rc
from random import choices as rcs

from utils import json_retreiver


class Person(object):
    """A randomly generated person in Doskvol"""

    def __init__(self, profession="both", heritage=None):
        self.profession = profession
        self.heritage = heritage
        self.gender = rc(json_retreiver("People/gender.json"))
        self.appearance = rc(json_retreiver("People/appearance.json"))
        self.goals = rc(json_retreiver("People/goals.json"))
        self.methods = rc(json_retreiver("People/methods.json"))
        self.style = rc(json_retreiver("People/style.json"))
        self.trait = rc(json_retreiver("People/traits.json"))
        self.interest = rc(json_retreiver("People/interests.json"))
        self.quirk = rc(json_retreiver("People/quirks.json"))
        self.first_name = rc(json_retreiver("People/first_names.json"))
        self.family_name = rc(json_retreiver("People/family_names.json"))
        self.alias = rc(json_retreiver("People/aliases.json"))

    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, rarity):
        if rarity.lower() == "rare":
            self._profession = rc(json_retreiver("People/rare_profession.json"))
        elif rarity.lower() == "common":
            self._profession = rc(json_retreiver("People/common_profession.json"))
        elif rarity.lower() == "both":
            self._profession = rc(
                json_retreiver("People/common_profession.json")
                + json_retreiver("People/rare_profession.json")
            )
        else:
            raise AttributeError("Purpose must be 'common', 'rare', or 'both'")

    @property
    def heritage(self):
        return self._heritage

    @heritage.setter
    def heritage(self, default_heritage):
        if default_heritage is None:
            h = rcs(json_retreiver("People/heritage.json"), weights=[50, 10, 5, 5, 5, 5])[0]
        else:
            h = default_heritage
        if h.lower() != "tycherosi":
            self._heritage = h
        else:
            self._heritage = h
            self.demonic_feature = rc(json_retreiver("Demons/demon_features.json"))

    def describe_person(self):
        """Returns a string that describes the building based on its attributes"""
        name = f"{self.first_name.capitalize()} '{self.alias.capitalize()}' {self.family_name.capitalize()}\n"
        description = f"A/An {self.appearance.lower()} {self.gender.lower()} {self.heritage.capitalize()}\n"
        quirk = f"Overall, they seem {self.trait.lower()} but are also {self.quirk.lower()}\n"
        interest = f"They are interested in {self.interest.lower()}\n"
        profession = f"They work as a {self.profession} and use {self.methods.lower()} to try and gain/cause {self.goals.lower()}.\n"
        if self.heritage.lower() == "tycherosi":
            demonic = f"Their Tycherosi heritage manifests as {self.demonic_feature.lower()}.\n"
            output = name + description + demonic + profession + quirk + interest
        else:
            output = name + description + profession + quirk + interest
        return output


if __name__ == "__main__":
    try:
        profession = sys.argv[1]
    except IndexError:  # no profession specified
        profession = "both"
    p = Person(profession)
    print(p.describe_person())
