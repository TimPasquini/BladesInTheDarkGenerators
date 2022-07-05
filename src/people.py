# people.py
"""The people class creates a randomly generated person utilizing
the rolling tables from the end of the Blades in the Dark rule book."""

import sys
from random import choice as rc
from random import choices as rcs

from utils import *


class Person(object):
    """A randomly generated person in Doskvol"""

    def __init__(
        self,
        profession=None,
        heritage=None,
        gender=None,
        appearance=None,
        goals=None,
        methods=None,
        style=None,
        trait=None,
        interest=None,
        quirk=None,
        first_name=None,
        family_name=None,
        alias=None,
    ):
        self.profession = two_choice_attribute_setter(
            profession,
            "rare",
            "common",
            "People/rare_profession.json",
            "People/common_profession.json",
        )
        self.heritage = heritage
        self.gender = simple_attribute_setter(gender, "People/gender.json")
        self.appearance = simple_attribute_setter(appearance, "People/appearance.json")
        self.goals = simple_attribute_setter(goals, "People/goals.json")
        self.methods = simple_attribute_setter(methods, "People/methods.json")
        self.style = simple_attribute_setter(style, "People/style.json")
        self.trait = simple_attribute_setter(trait, "People/traits.json")
        self.interest = simple_attribute_setter(interest, "People/interests.json")
        self.quirk = simple_attribute_setter(quirk, "People/quirks.json")
        self.first_name = simple_attribute_setter(first_name, "People/first_names.json")
        self.family_name = simple_attribute_setter(
            family_name, "People/family_names.json"
        )
        self.alias = simple_attribute_setter(alias, "People/aliases.json")

    def __str__(self):
        return (
            f"{self.first_name} '{self.alias}' {self.family_name}, a {self.profession}"
        )

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.profession}', '{self.heritage}', '{self.gender}', '{self.appearance}', '{self.goals}', '{self.methods}', '{self.style}', '{self.trait}', '{self.interest}', '{self.quirk}', '{self.first_name}', '{self.family_name}', '{self.alias}')"

    @property
    def heritage(self):
        return self._heritage

    @heritage.setter
    def heritage(self, default_heritage):
        if default_heritage is None:
            h = rcs(
                json_retreiver("../data/People/heritage.json"),
                weights=[50, 10, 5, 5, 5, 5],
            )[0]
        else:
            h = default_heritage
        if h.lower() != "tycherosi":
            self._heritage = h
        else:
            self._heritage = h
            self.demonic_feature = rc(
                json_retreiver("../data/Demons/demon_features.json")
            )

    def describe(self):
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
    print(p.describe())
