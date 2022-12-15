# scores.py
"""Uses the tables at the end of Blades in the Dark to generate a description
for a random score."""

from dataSets import SCORE
from generator import Generator


class Score(Generator):
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
        An unforeseen side effect of the score
    connection: str or None
        The relationship that connects the crew to the score
    faction: str or None
        A faction complicating the score

    Methods
    -------
    describe()
        Returns a formatted string describing the score
    """

    # re-roll information
    client_target_rerolls = ["Ghost of", "Possessed"]
    client_target_forbidden_rerolls = [
        "Ghost of",
        "Possessed",
        "Vampire",
        "Demon (disguised)",
        "Hollow",
    ]

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
        self.job = self.simple_attribute_setter(job, SCORE["JOBS"])
        self.twist = self.simple_attribute_setter(twist, SCORE["TWISTS"])
        self.connection = self.simple_attribute_setter(connection, SCORE["CONNECTIONS"])
        self.faction = self.simple_attribute_setter(faction, SCORE["FACTIONS"])

    def __str__(self):
        return f"{self.client} wants to {self.job} a {self.target}"

    def __repr__(self):
        return f"{self.__class__.__qualname__}('{self.client}', '{self.target}', '{self.job}', '{self.twist}', '{self.connection}', '{self.faction}')"

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, profession):
        client_profession = self.simple_attribute_setter(profession, SCORE["CLIENTS_TARGETS"])
        checked_profession = self.second_roll_check(
            client_profession,
            Score.client_target_rerolls,
            Score.client_target_forbidden_rerolls,
            SCORE["CLIENTS_TARGETS"],
        )
        self._client = checked_profession

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, profession):
        target_profession = self.simple_attribute_setter(profession, SCORE["CLIENTS_TARGETS"])
        checked_profession = self.second_roll_check(
            target_profession,
            Score.client_target_rerolls,
            Score.client_target_forbidden_rerolls,
            SCORE["CLIENTS_TARGETS"],
        )
        self._target = checked_profession

    def describe(self):
        """Returns a string that lays out a score based on its attributes"""
        client = self._reformat_ghost(self.client)
        target = self._reformat_ghost(self.target)
        output = f"""
{client.capitalize()} wants the crew to {self.job} {target}.
It's more complex because... {self.twist.lower()}.
A {self.connection} can tell you more about {self.faction.title()} involvement!"""
        return output

    @staticmethod
    def _reformat_ghost(client_target):
        if "Ghost of" in client_target:
            client_target = "a " + client_target
        return client_target


if __name__ == "__main__":
    s = Score()
    print(s.describe())
