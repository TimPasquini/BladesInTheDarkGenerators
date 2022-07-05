# scores.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random score."""

from random import choice as rc
from utils import *


class Score(object):
    """A randomly generated score for a crew in Doskvol to run"""

    def __init__(
        self,
        client=None,
        target=None,
        job=None,
        twist=None,
        connection=None,
        faction=None,
    ):
        self.client = client
        self.target = target
        self.job = simple_attribute_setter(job, "Scores/score_type.json")
        self.twist = simple_attribute_setter(twist, "Scores/complication.json")
        self.connection = simple_attribute_setter(connection, "Scores/connection.json")
        self.faction = simple_attribute_setter(faction, "Scores/factions.json")

    def __str__(self):
        return f"{self.client} wants to {self.job} a {self.target}"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.client}', '{self.target}', '{self.job}', '{self.twist}', '{self.connection}', '{self.faction}')"

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, profession):
        client_profession = simple_attribute_setter(
            profession, "Scores/client_target.json"
        )
        self._client = self._ghostcheck(client_profession)

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, profession):
        target_profession = simple_attribute_setter(
            profession, "Scores/client_target.json"
        )
        self._target = self._ghostcheck(target_profession)

    def _ghostcheck(self, profession):
        """If the client_target.json call returned 'Ghost of' this helper builds
        the rest of the string"""
        if profession != "Ghost of":
            return profession
        else:
            second_profession = rc(json_retreiver("../data/Scores/client_target.json"))
            while second_profession == "Ghost of":
                second_profession = rc(
                    json_retreiver("../data/Scores/client_target.json")
                )
            output = profession + " " + second_profession
            return output

    def describe(self):
        """Returns a string that lays out a score based on its attributes"""
        output = f"""
A/An {self.client.lower()} wants the crew to {self.job.lower()} a/an {self.target.lower()}.
It's more complex because... {self.twist}.
A {self.connection.lower()} can tell you more, but {self.faction.title()} are also involved!"""
        return output


if __name__ == "__main__":
    s = Score()
    print(s.describe())
