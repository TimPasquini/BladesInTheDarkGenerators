# cults.py
"""The cults class creates a randomly generated cult instance utilizing
the rolling tables from the end of the Blades in the Dark rule book."""

from random import choice as rc
from utils import json_retreiver


class Cult(object):
    """A randomly generated Cult operating in the city of Doskvol"""

    def __init__(self):
        self.god = rc(json_retreiver("../data/Cults/forgotten_gods.json"))
        self.practice = rc(json_retreiver("../data/Cults/cult_practices.json"))

    def describe_cult(self):
        """returns a string that describes a cult based on its attributes"""
        output = f"""
This is the cult of {self.god.title()}.
Their cultists follow an edict of:
    {self.practice.capitalize()}
        """
        return output


if __name__ == "__main__":
    c = Cult()
    print(c.describe_cult())
