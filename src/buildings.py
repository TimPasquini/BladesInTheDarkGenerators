# buildings.py
"""The building class creates a randomly generated building instance utilizing
the rolling tables from the end of the Blades in the Dark rule book."""

import sys

from utils import *


class Building(object):
    """A randomly generated building in the city of Doskvol. Uses both common
    and rare building purposes by default, 'rare' or 'common' can be passed to
    use the respective lists."""

    def __init__(
        self,
        purpose=None,
        material=None,
        exterior_detail=None,
        interior_detail_1=None,
        interior_detail_2=None,
    ):
        self.purpose = two_choice_attribute_setter(purpose, "rare", "common", "Buildings/rare_use.json", "Buildings/common_use.json")
        self.material = simple_attribute_setter(material, "Buildings/material.json")
        self.exterior_detail = simple_attribute_setter(
            exterior_detail, "Buildings/exterior_details.json"
        )
        self.interior_detail_1 = simple_attribute_setter(
            interior_detail_1, "Buildings/exterior_details.json"
        )
        self.interior_detail_2 = simple_attribute_setter(
            interior_detail_2, "Buildings/exterior_details.json"
        )

    def __str__(self):
        return f"a {self.material} {self.purpose}"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.purpose}', '{self.material}', '{self.exterior_detail}', '{self.interior_detail_1}', '{self.interior_detail_2}')"

    def describe(self):
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
        rarity = None
    b = Building(rarity)
    print(b.describe())
