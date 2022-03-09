# scores.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random score."""

from random import choice as rc
from utils import json_retreiver


class Score(object):
    """A randomly generated score for a crew in Doskvol to run"""

    def __init__(self):
        self.client = None
        self.target = None
        self.job = rc(json_retreiver("Scores/score_type.json"))
        self.twist = rc(json_retreiver("Scores/complication.json"))
        self.connection = rc(json_retreiver("Scores/connection.json"))
        self.faction = rc(json_retreiver("Scores/factions.json"))

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, dummy_arg):
        first_client = rc(json_retreiver("Scores/client_target.json"))
        if first_client != "Ghost of":
            self._client = first_client
        else:
            second_client = rc(json_retreiver("Scores/client_target.json"))
            while second_client == "Ghost of":
                second_client = rc(json_retreiver("Scores/client_target.json"))
            self._client = first_client + " " + second_client

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, dummy_arg):
        first_target = rc(json_retreiver("Scores/client_target.json"))
        if first_target != "Ghost of":
            self._target = first_target
        else:
            second_target = rc(json_retreiver("Scores/client_target.json"))
            while second_target == "Ghost of":
                second_target = rc(json_retreiver("Scores/client_target.json"))
            self._target = first_target + " " + second_target

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
