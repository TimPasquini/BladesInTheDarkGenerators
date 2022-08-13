# buildings.py
"""The building class creates a randomly generated building instance utilizing
the rolling tables from the end of the Blades in the Dark rule book."""

import sys

from utils import *
from dataSets import *


class Building(object):
    """A randomly generated building in the city of Doskvol.

    By default, all attributes are randomly created from the source lists. If
    a specific building with specific attributes is needed, any attribute can
    be overridden with a string.

    ...

    Attributes
    ----------
    purpose: str or None
        What the building is used for, pulls from rare and common lists when
        passed None, can pass str of "common" or "rare" to use respective list
    material: str or None
        What the building is made of
    exterior_detail: str or None
        A defining feature of the outside of the building
    interior_detail_1: str or None
        The first notable detail about the interior of the building
    interior_detail_2: str or None
        The second notable detail about the interior of the building

    Methods
    -------
    describe()
        Returns a formatted string describing the building
    """

    # reroll information
    interior_detail_rerolls = ["Threadbare", "Tattered", "Lush", "Comfortable", "Drafty", "Cold", "Stout", "Quiet", "Cozy", "Warm", "Vaulted", "Spacious", "Low", "Cramped", "Rickety", "Ramshackle", "Antique"]
    interior_detail_forbidden_rerolls = ["Threadbare", "Tattered", "Lush", "Comfortable", "Drafty", "Cold", "Stout", "Quiet", "Cozy", "Warm", "Vaulted", "Spacious", "Low", "Cramped", "Rickety", "Ramshackle", "Antique", "Dripping Water", "Creaking Floorboards", "Roaring Fires", "Smoky Lamps", "Buzzing Electric Lights", "Plants", "Flowers", "Artwork", "Elegant Finery", "Rough-Spun Simplicity", "Spartan Austerity"]

    def __init__(
        self,
        purpose=None,
        material=None,
        exterior_detail=None,
        interior_detail_1=None,
        interior_detail_2=None,
    ):
        self.purpose = two_choice_attribute_setter(
            purpose,
            "rare",
            "common",
            BUILDING_RARE_PURPOSES,
            BUILDING_COMMON_PURPOSES,
        )
        self.material = simple_attribute_setter(material, BUILDING_MATERIALS)
        self.exterior_detail = simple_attribute_setter(
            exterior_detail, BUILDING_EXTERIORS
        )
        self.interior_detail_1 = interior_detail_1
        self.interior_detail_2 = simple_attribute_setter(
            interior_detail_2, BUILDING_INTERIORS
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

    @property
    def interior_detail_1(self):
        return self._interior_detail_1

    @interior_detail_1.setter
    def interior_detail_1(self, detail):
        building_detail = simple_attribute_setter(detail, BUILDING_INTERIORS)
        checked_detail = second_roll_check(building_detail, Building.interior_detail_rerolls, Building.interior_detail_forbidden_rerolls, BUILDING_INTERIORS)
        self._interior_detail_1 = checked_detail

    @property
    def interior_detail_2(self):
        return self._interior_detail_2

    @interior_detail_2.setter
    def interior_detail_2(self, detail):
        building_detail = simple_attribute_setter(detail, BUILDING_INTERIORS)
        checked_detail = second_roll_check(building_detail, Building.interior_detail_rerolls, Building.interior_detail_forbidden_rerolls, BUILDING_INTERIORS)
        self._interior_detail_2 = checked_detail


if __name__ == "__main__":
    try:
        rarity = sys.argv[1]
    except IndexError:  # no building specified
        rarity = None
    b = Building(rarity)
    print(b.describe())
