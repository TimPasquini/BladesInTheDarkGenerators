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
from random import randint as ri
from random import choice as rc

from utils import *
from dataSets import *


class Leviathan(object):
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
    size: str or None
        Size defines how many distinct regions the leviathan has
    treasure_index: int or None
        Defines how many valuable treasures are on/in the leviathan
    spawn: str or LeviathanSpawn.form
        The type of Spawn the leviathan is generally known to produce

    Methods
    -------
    describe()
        Returns a formatted string using attributes to describe the
        leviathan and its associated spawn.
    """

    def __init__(
        self,
        activity=None,
        name=None,
        epithet=None,
        head_shape=None,
        body_shape=None,
        limb_shape=None,
        size=None,
        regions=None,
        treasure_index=None,
        treasures=None,
        spawn=None,
    ):
        self.activity = two_choice_attribute_setter(
            activity,
            "banal",
            "surreal",
            LEVIATHAN_BANAL_ACTIVITIES,
            LEVIATHAN_SURREAL_ACTIVITIES,
        )
        self.name = simple_attribute_setter(name, LEVIATHAN_NAMES)
        self.epithet = simple_attribute_setter(epithet, LEVIATHAN_EPITHETS)
        self.head_shape = simple_attribute_setter(head_shape, LEVIATHAN_SHAPES)
        self.body_shape = simple_attribute_setter(body_shape, LEVIATHAN_SHAPES)
        self.limb_shape = simple_attribute_setter(limb_shape, LEVIATHAN_SHAPES)
        self.size = size
        self.regions = regions
        self.treasure_index = treasure_index
        self.treasures = treasures
        self.spawn = LeviathanSpawn().form

    def __str__(self):
        return f"{self.name}, {self.epithet} leviathan"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.activity}', '{self.name}', '{self.epithet}', '{self.head_shape}', '{self.body_shape}', '{self.limb_shape}', '{self.size}', '{self.regions}', '{self.treasure_index}', '{self.treasures}', '{self.spawn}')"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, default_size):
        if default_size is None:
            leviathan_size = ri(1, 6) + 4
            self._size = leviathan_size
        else:
            self._size = default_size

    @property
    def regions(self):
        return self._regions

    @regions.setter
    def regions(self, default_regions):
        if default_regions is None:
            leviathan_regions = {}
            for num in range(1, self.size + 1):
                leviathan_regions[f"Region_{num}"] = rc(
                    json_retreiver(LEVIATHAN_DEMONIC_TRAITS)
                )
            self._regions = leviathan_regions
        else:
            self._regions = default_regions

    @property
    def treasure_index(self):
        return self._treasure_index

    @treasure_index.setter
    def treasure_index(self, default_index):
        if default_index is None:
            self._treasure_index = round(self.size / 4) + 1
        else:
            self._treasure_index = default_index

    @property
    def treasures(self):
        return self._treasures

    @treasures.setter
    def treasures(self, default_treasure):
        if default_treasure is None:
            leviathan_treasures = {}
            for num in range(1, self.treasure_index + 1):
                leviathan_treasures[f"treasure_{num}"] = rc(
                    json_retreiver(LEVIATHAN_TREASURES)
                )
            self._treasures = leviathan_treasures
        else:
            self._treasures = default_treasure

    def describe(self):
        intro = f"A leviathan is {self.activity.lower()} before you in the water.\n"
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
        spawn = f"This leviathan is known to spawn (a/an) {self.spawn}."
        output_string = (
            intro
            + form
            + size
            + "".join(region_description_list)
            + "".join(treasure_description_list)
            + spawn
        )
        return output_string


class LeviathanSpawn(object):
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

    def __init__(self, form=None):
        self.form = simple_attribute_setter(form, LEVIATHAN_SPAWN_FORMS)

    def __str__(self):
        return f"{self.form}, spawned by a leviathan."

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.form}')"

    @property
    def form(self):
        return self._form

    @form.setter
    def form(self, spawn_form):
        if spawn_form == "trigger three shapes":
            spawn_form = f"hybrid of a {self._grab_shape()}, a {self._grab_shape()}, and a {self._grab_shape()}"
        elif spawn_form == "trigger shape humanoid":
            spawn_form = f"humanoid {self._grab_shape()}"
        elif spawn_form == "trigger shape inside-out":
            spawn_form = f"{self._grab_shape()} turned inside-out"
        elif spawn_form == "trigger shape flying":
            spawn_form = f"flying {self._grab_shape()}"
        elif spawn_form == "trigger ghosts":
            spawn_form = f"multitude of ghosts. There is/are (a/an) {self._grab_ghost()}dead sailors and other spectral eminations appear"
        elif spawn_form == "trigger demon":
            spawn_form = f"{self._grab_demon()}"
        self._form = spawn_form

    def _grab_shape(self):
        return rc(json_retreiver(LEVIATHAN_SHAPES))

    def _grab_ghost(self):
        trait = rc(json_retreiver(GHOST_TRAITS))
        effect = rc(json_retreiver(GHOST_EFFECTS))
        return f"{effect.lower()} when these {trait.lower()} "

    def _grab_demon(self):
        feature = rc(json_retreiver(DEMON_FEATURES))
        aspect = rc(json_retreiver(DEMON_ASPECTS))
        affinity = rc(json_retreiver(DEMON_AFFINITYS))
        demon = f"{aspect.lower()} {affinity.lower()} demon with {feature.lower()}"
        return demon

    def describe(self):
        """returns a string describing the spawn"""
        output = f"The leviathan releases a new spawn, it emits (a/an) {self.form}"
        return output


if __name__ == "__main__":
    try:
        leviathan_activity = sys.argv[1]
    except IndexError:  # no activity specified
        leviathan_activity = None
    lev = Leviathan(leviathan_activity)
    print(lev.describe())
