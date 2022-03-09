# people.py
"""The people class creates a randomly generated person utilizing
the rolling tables from the end of the Blades in the Dark rule book."""

import sys
from random import choice as rc
from random import choices as rcs

from utils import json_retreiver


class Person(object):
    """A randomly generated person in Doskvol"""

    def __init__(self, profession="both"):
        self.profession = (
            profession  # TODO: @property & setter to select from appropriate list
        )
        self.heritage = rcs(
            json_retreiver("People/heritage.json"), weights=[50, 10, 5, 5, 5, 5]
        )[0]
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
