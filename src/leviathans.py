# leviathans.py
"""Uses the tables in the Leviathan Song Supplement to generate a description
for a leviathan and leviathan spawn.

...

Classes
-------
Leviathan
    The base class for all the leviathans in Doskvol
LeviathanSpawn
    The base class for leviathan spawn
"""

import sys
from typing import Union
from random import randint

from dataSets import LEVIATHAN, DEMON, GHOST
from generator import Generator


class Leviathan(Generator):
    """A randomly generated leviathan that inhabits the Void Sea.

    By default, all attributes are randomly created from the source lists. If
    a specific Leviathan with specific attributes is needed, any attribute can
    be overridden with a string.

    ...

    Attributes
    ----------
    activity: str or None
        What a leviathan is doing when it is first spotted, pulls from banal and
        surreal lists when passed None, can pass str of "banal" or "surreal" to
        use respective list
    name: str or None
        The supposed name of the leviathan
    epithet: str or None
        The nickname or title of the leviathan
    head_shape: str or None
        The form its head resembles, usually a sea creature
    body_shape: str or None
        The form its body resembles, usually a sea creature
    limb_shape: str or None
        How the leviathan moves around, limbs, usually a sea creature's
    size: int or None
        Size defines how many distinct regions the leviathan has
    regions: dict or None
        A dictonary that holds the types of regions present on the leviathan
    treasure_index: int or None
        Defines how many valuable treasures are on/in the leviathan
    spawn: LeviathanSpawn object or None
        The type of Spawn the leviathan is generally known to produce

    Methods
    -------
    describe()
        Returns a formatted string using attributes to describe the
        leviathan and its associated spawn.
    """

    def __init__(
        self,
        activity: str | None = None,
        name: str | None = None,
        epithet: str | None = None,
        head_shape: str | None = None,
        body_shape: str | None = None,
        limb_shape: str | None = None,
        size: int | None = None,
        regions: dict | None = None,
        treasure_index: int | None = None,
        treasures: dict | None = None,
        spawn: Union["LeviathanSpawn", None] = None,
    ):
        self.activity = self.two_choice_attribute_setter(
            activity,
            "banal",
            "surreal",
            LEVIATHAN["BANAL_ACTIVITIES"],
            LEVIATHAN["SURREAL_ACTIVITIES"],
        )
        self.name = self.simple_attribute_setter(name, LEVIATHAN["NAMES"])
        self.epithet = self.simple_attribute_setter(epithet, LEVIATHAN["EPITHETS"])
        self.head_shape = self.simple_attribute_setter(head_shape, LEVIATHAN["SHAPES"])
        self.body_shape = self.simple_attribute_setter(body_shape, LEVIATHAN["SHAPES"])
        self.limb_shape = self.simple_attribute_setter(limb_shape, LEVIATHAN["SHAPES"])
        self.size = size if size is not None else Leviathan._generate_random_size()
        self.regions = regions if regions is not None else self._generate_regions()
        self.treasure_index = (
            treasure_index
            if treasure_index is not None
            else self._generate_treasure_index()
        )
        self.treasures = (
            treasures if treasures is not None else self._generate_treasures()
        )
        self.spawn = spawn

    def __str__(self):
        return f"{self.name}, {self.epithet} leviathan"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.activity}', '{self.name}', '{self.epithet}', '{self.head_shape}', '{self.body_shape}', '{self.limb_shape}', '{self.size}', '{self.regions}', '{self.treasure_index}', '{self.treasures}', '{self.spawn}')"

    @property
    def spawn(self) -> Union["LeviathanSpawn", None]:
        return self._spawn

    @spawn.setter
    def spawn(self, default_spawn: Union["LeviathanSpawn", None]):
        if default_spawn is None:
            default_spawn = LeviathanSpawn()
        if isinstance(default_spawn, LeviathanSpawn):
            default_spawn = default_spawn
        self._spawn = default_spawn

    @staticmethod
    def _generate_random_size() -> int:
        return randint(1, 6) + 4

    def _generate_treasure_index(self) -> int:
        return int(round(self.size / 4) + 1)

    def _generate_regions(self) -> dict:
        leviathan_regions = {}
        for num in range(1, self.size + 1):
            leviathan_regions[f"Region_{num}"] = self.simple_attribute_setter(
                None, LEVIATHAN["DEMONIC_TRAITS"]
            )
        return leviathan_regions

    def _generate_treasures(self) -> dict:
        leviathan_treasures = {}
        for num in range(1, self.treasure_index + 1):
            leviathan_treasures[f"treasure_{num}"] = self.simple_attribute_setter(
                None, LEVIATHAN["TREASURES"]
            )
        return leviathan_treasures

    def describe(self) -> str:
        intro = f"A leviathan is {self.activity} before you in the water.\n"
        name = f"It is none other than {self.name.capitalize()}, '{self.epithet.title()}.'\n"
        form = f"This leviathan has the head of a {self.head_shape}, the body of a {self.body_shape} and moves on the limbs of a {self.limb_shape}.\n"
        size = f"There are {self.size} distinct regions on this leviathans body:\n"
        # create the list for printing region descriptions from the region dictionary
        region_description_list = []
        for num in range(1, self.size + 1):
            region_trait = self.regions[f"Region_{num}"]
            region_description = f"Region {num} is notable for its {region_trait}.\n"
            region_description_list.append(region_description)
        # create the list for printing leviathan's treasures
        treasure_description_list = [
            "Braving the regions could lead to valuable treasure:\n"
        ]
        for num in range(1, self.treasure_index + 1):
            active_treasure = self.treasures[f"treasure_{num}"]
            treasure_description = f"{active_treasure}.\n"
            treasure_description_list.append(treasure_description)
        spawn = f"This leviathan is known to spawn {self.spawn.form}."
        output_string = (
            intro
            + name
            + form
            + size
            + "".join(region_description_list)
            + "".join(treasure_description_list)
            + spawn
        )
        return output_string


class LeviathanSpawn(Generator):
    """A randomly generated spawn of a Leviathan

    By default, all attributes are randomly created from the source lists. If
    a specific Leviathan Spawn with specific attributes is needed, any attribute
    can be overridden with a string.

    ...

    Attributes
    ----------
    form: str or None
        The physical description of a leviathan spawn

    Methods
    -------
    _grab_shape()
        Returns an overall sea-creature shape for hybrid spawn
    _grab_ghost()
        Returns a formatted string of a ghost trait and effect for ghostly spawn
    _grab_demon()
        Returns a formatted string with a demonic feature, aspect, and affinity
        for a demonic spawn
    describe()
        Returns a formatted string describing the leviathan spawn
    """

    def __init__(self, form: str | None = None):
        self.form = self.simple_attribute_setter(form, LEVIATHAN["SPAWN_FORMS"])

    def __str__(self):
        return f"{self.form}, spawned by a leviathan."

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.form}')"

    @property
    def form(self):
        return self._form

    @form.setter
    def form(self, spawn_form: str | None):
        # lambda blocks instantiation at dictionary creation, instantiation is handled at lookup
        complex_forms = {
            "trigger three shapes": lambda: f"a hybrid of a {self._grab_shape()}, {self._grab_shape()}, and {self._grab_shape()}",
            "trigger shape humanoid": lambda: f"a humanoid {self._grab_shape()}",
            "trigger shape inside-out": lambda: f"a {self._grab_shape()} turned inside-out",
            "trigger shape flying": lambda: f"a flying {self._grab_shape()}",
            "trigger ghosts": lambda: f"a multitude of ghosts. There is {self._grab_ghost()} dead sailors and other spectral emanations appear",
            "trigger demon": lambda: self._grab_demon(),
        }
        # see if a complex form needs to be built or continue with the simple form
        self._form = complex_forms.get(spawn_form, lambda: spawn_form)()

    def _grab_shape(self):
        return self.simple_attribute_setter(None, LEVIATHAN["SHAPES"])

    def _grab_ghost(self):
        trait = self.simple_attribute_setter(None, GHOST["TRAITS"])
        effect = self.simple_attribute_setter(None, GHOST["EFFECTS"])
        return f"{effect} when these {trait}"

    def _grab_demon(self):
        feature = self.simple_attribute_setter(None, DEMON["FEATURES"])
        aspect = self.simple_attribute_setter(None, DEMON["ASPECTS"])
        affinity = self.simple_attribute_setter(None, DEMON["AFFINITIES"])
        demon = f"{aspect} {affinity} demon with {feature}"
        return demon

    def describe(self) -> str:
        """returns a string describing the spawn"""
        output = f"The leviathan releases a new spawn, it emits {self.form}"
        return output


if __name__ == "__main__":
    try:
        leviathan_activity = sys.argv[1]
    except IndexError:  # no activity specified
        leviathan_activity = None
    lev = Leviathan(leviathan_activity)
    print(lev.describe())
