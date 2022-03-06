# buildings.py
"""The building class creates a randomly generated building instance utilizing
the rolling tables from the end of the Blades in the Dark rule book."""

import sys
from random import choice as rc

from utils import json_retreiver


class Building():
    """A randomly generated building in the city of Doskvol."""

    def __init__(self, purpose="both"):
        self.material = rc(json_retreiver("Buildings/material.json"))
        self.exterior_detail = rc(json_retreiver("Buildings/exterior_details.json"))
        self.interior_detail_1 = rc(json_retreiver("Buildings/exterior_details.json"))
        self.interior_detail_2 = rc(json_retreiver("Buildings/exterior_details.json"))
        self._purpose = purpose

    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, usage):
        if usage.lower() == "rare":
            self._purpose = rc(json_retreiver("Buildings/rare_use.json"))
        if usage.lower() == "common":
            self._purpose = rc(json_retreiver("Buildings/common_use.json"))
        if usage.lower() == "both":
            self._purpose == rc(
                json_retreiver("Buildings/common_use.json")
                + json_retreiver("Buildings/rare_use.json")
            )
