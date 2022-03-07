# buildings.py
"""The building class creates a randomly generated building instance utilizing
the rolling tables from the end of the Blades in the Dark rule book."""

import sys
from random import choice as rc

from utils import json_retreiver


class Building(object):
    """A randomly generated building in the city of Doskvol."""

    def __init__(self, purpose="both"):
        self.material = rc(json_retreiver("Buildings/material.json"))
        self.exterior_detail = rc(json_retreiver("Buildings/exterior_details.json"))
        self.interior_detail_1 = rc(json_retreiver("Buildings/exterior_details.json"))
        self.interior_detail_2 = rc(json_retreiver("Buildings/exterior_details.json"))
        self.purpose = purpose

    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, usage):
        if usage.lower() == "rare":
            self._purpose = rc(json_retreiver("Buildings/rare_use.json"))
        elif usage.lower() == "common":
            self._purpose = rc(json_retreiver("Buildings/common_use.json"))
        elif usage.lower() == "both":
            self._purpose = rc(
                json_retreiver("Buildings/common_use.json")
                + json_retreiver("Buildings/rare_use.json")
            )
        else:
            raise AttributeError("Purpose must be 'common', 'rare', or 'both'")

    def describe_building(self):
        """Returns a string that describes the building based on its attributes"""
        output = (
            f"This {self.material.lower()} {self.purpose.lower()} "
            f"building is decorated with {self.exterior_detail.lower()}.\n"
            f"It is notable for its {self.interior_detail_1.lower()} "
            f"and {self.interior_detail_2.lower()}"
        )
        return output


if __name__ == "__main__":
    try:
        rarity = sys.argv[1]
    except IndexError:  # no building specified
        rarity = "both"
    b = Building(rarity)
    print(b.describe_building())
