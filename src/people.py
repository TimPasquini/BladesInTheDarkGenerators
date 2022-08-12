# people.py
"""The people class creates a randomly generated person utilizing
the rolling tables from the end of the Blades in the Dark rule book."""

import sys
from random import choice as rc
from random import choices as rcs

from utils import *
from dataSets import *


class Person(object):
    """A randomly generated person in Doskvol

    By default, all attributes are randomly created from the source lists. If
    a specific person with specific attributes is needed, any attribute can
    be overridden with a string.

    ...

    Attributes
    ----------
    profession: str or None
        The paid occupation of this Person, pulls from rare and common lists if
        passed None, can pass str of "common" or "rare" to use respective list
    heritage: str or None
        Ethnic origin within the Shattered Isles
    gender: str or None
        The chosen gender this Person presents as
    appearance: str or None
        An adjective describing a major visual feature of this Person
    goals: str or None
        A motivating force for this Person
    methods: str or None
        The preferred technique this Person uses to further their goals
    style: str or None
        A notable piece of clothing or accessory worn by this Person
    trait: str or None
        An adjective describing a major personality feature
    interest: str or None
        A curosity, focus, or concern of this Person
    quirk: str or None
        An additional feature to make this Person more interesting
    first_name: str or None
        A Person's given name
    family_name: str or None
        A Person's surname
    alias: str or None
        A nickname, familiar name, assumed identity, or nom de gurre

    Methods
    -------
    describe()
        Returns a formatted string using attributes to describe a Person
    """

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
            RARE_PROFESSIONS,
            COMMON_PROFESSIONS,
        )
        self.heritage = heritage
        self.gender = simple_attribute_setter(gender, GENDERS)
        self.appearance = simple_attribute_setter(appearance, APPEARANCES)
        self.goals = simple_attribute_setter(goals, GOALS)
        self.methods = simple_attribute_setter(methods, METHODS)
        self.style = simple_attribute_setter(style, STYLES)
        self.trait = simple_attribute_setter(trait, TRAITS)
        self.interest = simple_attribute_setter(interest, INTERESTS)
        self.quirk = simple_attribute_setter(quirk, QUIRKS)
        self.first_name = simple_attribute_setter(first_name, FIRST_NAMES)
        self.family_name = simple_attribute_setter(family_name, FAMILY_NAMES)
        self.alias = simple_attribute_setter(alias, ALIASES)

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
            h = rcs(json_retreiver(HERITAGES), weights=[50, 10, 5, 5, 5, 5])[0]
        else:
            h = default_heritage
        if h.lower() != "tycherosi":
            self._heritage = h
        else:
            self._heritage = h
            self.demonic_feature = rc(json_retreiver(DEMON_FEATURES))

    def describe(self):
        """Returns a string that describes the building based on its attributes"""
        name = f"{self.first_name.capitalize()} '{self.alias.capitalize()}' {self.family_name.capitalize()}\n"
        description = f"A/An {self.appearance.lower()} {self.gender.lower()} {self.heritage.capitalize()} wearing (a/an) {self.style}\n"
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
        profession = None
    p = Person(profession)
    print(p.describe())
