# leviathans.py
"""Uses the tables in the Leviathan Song Supplement to generate a description
for a leviathan and leviathan spawn."""

import sys
from random import randint as ri
from random import choice as rc

from utils import json_retreiver


class Leviathan(object):
    """A randomly generated leviathan"""

    def __init__(self, activity="both", size=None, treasure_index=None):
        self.activity = activity
        self.name = rc(json_retreiver("Leviathan/leviathan_names.json"))
        self.epithet = rc(json_retreiver("Leviathan/epithet.json"))
        self.head_shape = self._grab_shape()
        self.body_shape = self._grab_shape()
        self.limb_shape = self._grab_shape()
        self.size = size
        self.treasure_index = treasure_index
        self.spawn = LeviathanSpawn().form

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, leviathan_activity):
        if leviathan_activity.lower() == "banal":
            self._activity = rc(json_retreiver("Leviathan/banal_activity.json"))
        elif leviathan_activity.lower() == "surreal":
            self._activity = rc(json_retreiver("Leviathan/surreal_activity.json"))
        elif leviathan_activity.lower() == "both":
            self._activity = rc(
                json_retreiver("Leviathan/banal_activity.json")
                + json_retreiver("Leviathan/surreal_activity.json")
            )
        else:
            raise AttributeError(
                "Leviathan acivity must be 'banal', 'surreal', or 'both'"
            )

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
        leviathan_regions = {}
        for num in range(1, self.size + 1):
            leviathan_regions[f"Region_{num}"] = rc(
                json_retreiver("Leviathan/leviathan_demon_traits.json")
            )
        self.regions = leviathan_regions

    @property
    def treasure_index(self):
        return self._treasure_index

    @treasure_index.setter
    def treasure_index(self, default_index):
        if default_index is None:
            self._treasure_index = round(self.size / 4) + 1
        else:
            self._treasure_index = default_index
        leviathan_treasures = {}
        for num in range(1, self.treasure_index + 1):
            leviathan_treasures[f"treasure_{num}"] = rc(
                json_retreiver("Leviathan/leviathan_treasures.json")
            )
        self.treasures = leviathan_treasures

    def _grab_shape(self):
        return rc(json_retreiver("Leviathan/shapes.json"))

    def describe_leviathan(self):
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
    """A randomly generated spawn of a Leviathan"""

    def __init__(self):
        self.form = rc(json_retreiver("Leviathan/leviathan_spawn.json"))

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
        return rc(json_retreiver("Leviathan/shapes.json"))

    def _grab_ghost(self):
        trait = rc(json_retreiver("Ghosts/ghost_traits.json"))
        effect = rc(json_retreiver("Ghosts/ghostly_effect.json"))
        return f"{effect.lower()} when these {trait.lower()} "

    def _grab_demon(self):
        feature = rc(json_retreiver("Demons/demon_features.json"))
        aspect = rc(json_retreiver("Demons/demonic_aspect.json"))
        affinity = rc(json_retreiver("Demons/demonic_affinity.json"))
        demon = f"{aspect.lower()} {affinity.lower()} demon with {feature.lower()}"
        return demon

    def describe_spawn(self):
        """returns a string describing the spawn"""
        output = (
            f"The leviathan releases a new spawn, it emits (a/an) {self.form}"
        )
        return output


if __name__ == "__main__":
    try:
        leviathan_activity = sys.argv[1]
    except IndexError:  # no activity specified
        leviathan_activity = "both"
    lev = Leviathan(leviathan_activity)
    print(lev.describe_leviathan())
