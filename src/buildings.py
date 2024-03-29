# buildings.py
"""The building class creates a randomly generated building instance utilizing
the rolling tables from the end of the Blades in the Dark rule book."""

import sys

from dataSets import BUILDING
from generator import Generator


class Building(Generator):
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

    # re-roll information
    interior_detail_rerolls = [
        "Threadbare",
        "Tattered",
        "Lush",
        "Comfortable",
        "Drafty",
        "Cold",
        "Stout",
        "Quiet",
        "Cozy",
        "Warm",
        "Vaulted",
        "Spacious",
        "Low",
        "Cramped",
        "Rickety",
        "Ramshackle",
        "Antique",
    ]
    interior_detail_forbidden_rerolls = interior_detail_rerolls + [
        "Dripping Water",
        "Creaking Floorboards",
        "Roaring Fires",
        "Smoky Lamps",
        "Buzzing Electric Lights",
        "Plants",
        "Flowers",
        "Artwork",
        "Elegant Finery",
        "Rough-Spun Simplicity",
        "Spartan Austerity",
    ]

    def __init__(
        self,
        purpose: str | None = None,
        material: str | None = None,
        exterior_detail: str | None = None,
        interior_detail_1: str | None = None,
        interior_detail_2: str | None = None,
    ):
        self.purpose = self.two_choice_attribute_setter(
            purpose,
            "rare",
            "common",
            BUILDING["RARE_PURPOSES"],
            BUILDING["COMMON_PURPOSES"],
        )
        self.material = self.simple_attribute_setter(material, BUILDING["MATERIALS"])
        self.exterior_detail = self.simple_attribute_setter(
            exterior_detail, BUILDING["EXTERIORS"]
        )
        self.interior_detail_1 = interior_detail_1
        self.interior_detail_2 = self.simple_attribute_setter(
            interior_detail_2, BUILDING["INTERIORS"]
        )

    def __str__(self):
        return f"a {self.material} {self.purpose}"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.purpose}', '{self.material}', '{self.exterior_detail}', '{self.interior_detail_1}', '{self.interior_detail_2}')"

    def describe(self) -> str:
        """Returns a string that describes the building based on its attributes"""
        output = (
            f"A {self.material} {self.purpose} building.\n"
            f"The building exterior is decorated with {self.exterior_detail}.\n"
            f"It is notable for its {self.interior_detail_1} "
            f"and {self.interior_detail_2}"
        )
        return output

    @property
    def interior_detail_1(self):
        return self._interior_detail_1

    @interior_detail_1.setter
    def interior_detail_1(self, detail: str | None):
        self._interior_detail_1 = self._set_valid_interior_detail(detail)

    @property
    def interior_detail_2(self):
        return self._interior_detail_2

    @interior_detail_2.setter
    def interior_detail_2(self, detail: str | None):
        self._interior_detail_2 = self._set_valid_interior_detail(detail)

    def _set_valid_interior_detail(self, detail: str | None) -> str:
        """Called by the setters to return a valid and complete building detail"""
        # validate that initial detail is not None, or generate a random choice if it is
        initial_detail = self.simple_attribute_setter(detail, BUILDING["INTERIORS"])
        # Check if the initial detail needs additional rolls to reach a "complete" detail
        return self.second_roll_check(
            initial_detail,
            Building.interior_detail_rerolls,
            Building.interior_detail_forbidden_rerolls,
            BUILDING["INTERIORS"],
        )


if __name__ == "__main__":
    try:
        rarity = sys.argv[1]
    except IndexError:  # no building specified
        rarity = None
    b = Building(rarity)
    print(b.describe())
