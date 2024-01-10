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
    client_target_rerolls = ["a Ghost of", "Possessed"]
    client_target_forbidden_rerolls = client_target_rerolls + [
        "Vampire",
        "Demon (disguised)",
        "Hollow",
    ]

    def __init__(
        self,
        client: str | None = None,
        target: str | None = None,
        job: str | None = None,
        twist: str | None = None,
        connection: str | None = None,
        faction: str | None = None,
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
        self._client = self._set_client_or_target(profession)

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, profession):
        self._target = self._set_client_or_target(profession)

    def _set_client_or_target(self, profession: str) -> str:
        initial_profession = self.simple_attribute_setter(
            profession, SCORE["CLIENTS_TARGETS"]
        )
        return self.second_roll_check(
            initial_profession,
            Score.client_target_rerolls,
            Score.client_target_forbidden_rerolls,
            SCORE["CLIENTS_TARGETS"],
        )

    def describe(self) -> str:
        """Returns a string that lays out a score based on its attributes"""
        client = self._reformat_ghost(self.client)
        target = self._reformat_ghost(self.target)
        output = f"""
{client.capitalize()} wants the crew to {self.job} {target}.
It's more complex because... {self.twist}.
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
