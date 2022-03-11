# scores.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random score."""

from random import choice as rc
from utils import json_retreiver


class Score(object):
    """A randomly generated score for a crew in Doskvol to run"""

    def __init__(self, client=None, target=None):
        self.client = client
        self.target = target
        self.job = rc(json_retreiver("../data/Scores/score_type.json"))
        self.twist = rc(json_retreiver("../data/Scores/complication.json"))
        self.connection = rc(json_retreiver("../data/Scores/connection.json"))
        self.faction = rc(json_retreiver("../data/Scores/factions.json"))

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, profession):
        client_profession = self._career_advisor(profession)
        self._client = self._ghostcheck(client_profession)

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, profession):
        target_profession = self._career_advisor(profession)
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

    def _career_advisor(self, profession):
        """If a profession for a target or client isn't specified, this will
        select one."""
        if profession is None:
            profession = rc(json_retreiver("../data/Scores/client_target.json"))
        return profession

    def describe_score(self):
        """Returns a string that lays out a score based on its attributes"""
        output = f"""
A/An {self.client.lower()} wants the crew to {self.job.lower()} a/an {self.target.lower()}.
It's more complex because... {self.twist}.
A {self.connection.lower()} can tell you more, but {self.faction.title()} are also involved!"""
        return output


if __name__ == "__main__":
    s = Score()
    print(s.describe_score())
