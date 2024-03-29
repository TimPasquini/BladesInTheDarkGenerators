# people.py
"""The people class creates a randomly generated person utilizing
the rolling tables from the end of the Blades in the Dark rule book."""

import sys
from random import choices as rcs

from dataSets import PEOPLE, DEMON
from generator import Generator


class Person(Generator):
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
        A curiosity, focus, or concern of this Person
    quirk: str or None
        An additional feature to make this Person more interesting
    first_name: str or None
        A Person's given name
    family_name: str or None
        A Person's surname
    alias: str or None
        A nickname, familiar name, assumed identity, or nom de guerre

    Methods
    -------
    describe()
        Returns a formatted string using attributes to describe a Person
    """

    def __init__(
        self,
        profession: str | None = None,
        heritage: str | None = None,
        gender: str | None = None,
        appearance: str | None = None,
        goals: str | None = None,
        methods: str | None = None,
        style: str | None = None,
        trait: str | None = None,
        interest: str | None = None,
        quirk: str | None = None,
        first_name: str | None = None,
        family_name: str | None = None,
        alias: str | None = None,
    ):
        self.profession = self.two_choice_attribute_setter(
            profession,
            "rare",
            "common",
            PEOPLE["RARE_PROFESSIONS"],
            PEOPLE["COMMON_PROFESSIONS"],
        )
        self.heritage = heritage
        self.gender = self.simple_attribute_setter(gender, PEOPLE["GENDERS"])
        self.appearance = self.simple_attribute_setter(
            appearance, PEOPLE["APPEARANCES"]
        )
        self.goals = self.simple_attribute_setter(goals, PEOPLE["GOALS"])
        self.methods = self.simple_attribute_setter(methods, PEOPLE["METHODS"])
        self.style = self.simple_attribute_setter(style, PEOPLE["STYLES"])
        self.trait = self.simple_attribute_setter(trait, PEOPLE["TRAITS"])
        self.interest = self.simple_attribute_setter(interest, PEOPLE["INTERESTS"])
        self.quirk = self.simple_attribute_setter(quirk, PEOPLE["QUIRKS"])
        self.first_name = self.simple_attribute_setter(
            first_name, PEOPLE["FIRST_NAMES"]
        )
        self.family_name = self.simple_attribute_setter(
            family_name, PEOPLE["FAMILY_NAMES"]
        )
        self.alias = self.simple_attribute_setter(alias, PEOPLE["ALIASES"])

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
    def heritage(self, default_heritage: str | None):
        if not isinstance(default_heritage, str):
            default_heritage = rcs(
                self.json_retriever(PEOPLE["HERITAGES"]), weights=[50, 10, 5, 5, 5, 5]
            )[0]
        self._heritage = default_heritage
        self._set_demonic_feature_if_tycherosi()

    def _set_demonic_feature_if_tycherosi(self):
        if self._heritage.lower() == "tycherosi":
            self.demonic_feature = self.simple_attribute_setter(None, DEMON["FEATURES"])

    def describe(self) -> str:
        """Returns a string that describes the building based on its attributes"""
        name = f"{self.first_name.capitalize()} '{self.alias.capitalize()}' {self.family_name.capitalize()}\n"
        description = f"This {self.appearance} {self.gender} {self.heritage.capitalize()} is {self.style}\n"
        quirk = f"Overall, they seem {self.trait} but also {self.quirk}.\n"
        interest = f"They are interested in {self.interest}\n"
        profession = f"They work as a {self.profession} and use {self.methods} to try and gain/cause {self.goals}.\n"
        if self.heritage.lower() == "tycherosi":
            demonic = f"Their Tycherosi heritage manifests as {self.demonic_feature}.\n"
            output = name + description + demonic + profession + quirk + interest
        else:
            output = name + description + profession + quirk + interest
        return output


if __name__ == "__main__":
    try:
        employment = sys.argv[1]
    except IndexError:  # no profession specified
        employment = None
    p = Person(employment)
    print(p.describe())
