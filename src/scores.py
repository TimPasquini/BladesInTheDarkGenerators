# scores.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random score."""

from random import choice as rc
from utils import *
from dataSets import *


class Score(object):
    """A randomly generated score for a crew in Doskvol to run

    By default, all attributes are randomly created from the source lists. If
    a specific Score with specific attributes is needed, any attribute can
    be overridden with a string.

    ...

    Attributes
    ----------
    client: str or None
        The person giving the job
    target: str or None
        The victim of the score
    job: str or None
        The type of score, the method of enacting it
    twist: str or None
        An unforseen side-effect of the score
    connection: str or None
        The relationship that connects the crew to the score
    faction: str or None
        A faction complicating the score

    Methods
    -------
    _ghostcheck()
        If the client or target is initially assigned "Ghost of" this completes
        the process and adds another client/target to the end of "Ghost of"
    describe()
        Returns a formatted string describing the score
    """

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
        self.job = simple_attribute_setter(job, SCORE_JOBS)
        self.twist = simple_attribute_setter(twist, SCORE_TWISTS)
        self.connection = simple_attribute_setter(connection, SCORE_CONNECTIONS)
        self.faction = simple_attribute_setter(faction, SCORE_FACTIONS)

    def __str__(self):
        return f"{self.client} wants to {self.job} a {self.target}"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.client}', '{self.target}', '{self.job}', '{self.twist}', '{self.connection}', '{self.faction}')"

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, profession):
        client_profession = simple_attribute_setter(profession, SCORE_CLIENTS_TARGETS)
        checked_profession = self._ghostcheck(client_profession)
        checked_profession = self._possessedcheck(checked_profession)
        self._client = checked_profession


    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, profession):
        target_profession = simple_attribute_setter(profession, SCORE_CLIENTS_TARGETS)
        checked_profession = self._ghostcheck(target_profession)
        checked_profession = self._possessedcheck(checked_profession)
        self._target = checked_profession

    def _ghostcheck(self, profession):
        """If the client_target.json call returned 'Ghost of' this helper builds
        the rest of the string"""
        if profession != "Ghost of":
            return profession
        else:
            second_profession = rc(json_retreiver(SCORE_CLIENTS_TARGETS))
            while (second_profession == "Ghost of") or (second_profession == "Possessed"):
                second_profession = rc(json_retreiver(SCORE_CLIENTS_TARGETS))
            output = profession + " " + second_profession
            return output

    def _possessedcheck(self, profession):
        """If the client_target.json call returned 'Possessed' this helper builds
        the rest of the string"""
        if profession != "Possessed":
            return profession
        else:
            second_profession = rc(json_retreiver(SCORE_CLIENTS_TARGETS))
            while (second_profession == "Ghost of") or (second_profession == "Possessed"):
                second_profession = rc(json_retreiver(SCORE_CLIENTS_TARGETS))
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
