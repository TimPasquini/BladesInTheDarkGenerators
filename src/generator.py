"""
Base Class for methods used by all Generators.

...

Functions
---------
json_retriever: str
    Used to assign the contents of a .json to a variable
history_log: str
    writes any output string to an external text document
simple_attribute_setter: str or None
    used by setters to pull from .json if None is passed
two_choice_attribute_setter: string or None
    used by setters when there are two potential .json files to use
second_roll_check:
    used when there are incompatable or compounding elements in a dataset
"""

import json
from abc import ABC, abstractmethod

from random import choice


class Generator(ABC):
    """This base class carries the underlying utility methods used across all generators."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def describe(self):
        pass

    @staticmethod
    def json_retriever(json_filepath: str):
        """Use to assign the contents of a .json to a variable.

        This is a quick way to pull the contents of a .json file into the
        program. The type returned is based on the contents of the .json

        Arguments
        ---------
        json_filepath: str
            This should be the entire filepath including filename
        """
        with open(json_filepath) as f:
            return json.load(f)

    @staticmethod
    def history_log(output: str):
        """Writes any output string to an external text document.

        Dumps a string to file, history.txt and adds linebreaks so that it
        can be referenced if the program crashed or was closed. Primarily
        for debugging.

        Arguments
        ---------
        output: str
            This should be the string you want dumped to the history file
        """
        filename = "history.txt"
        with open(filename, "a") as f:
            f.write(output)
            f.write("\n\n")

    @staticmethod
    def simple_attribute_setter(attribute: str | None, path: str) -> str | None:
        """Used by setters to pull from .json if None is passed.

        If you don't define an optional attribute for instantiation, this
        function will make a random selection from a list stored in a .json
        file.

        Arguments
        ---------
        attribute: str or None
            A string will be returned unaltered but None will trigger the
            random selection code.
        path: str
            Since all .json files are stored in /data/ the path should be:
                "[Class]/[attribute.json]"
                or
                "[Class]/[ChildClass]/[attribute.json]"
        """
        if attribute is None:
            attribute = choice(Generator.json_retriever(path))
        return attribute

    @staticmethod
    def two_choice_attribute_setter(
        attribute: str | None, option_1: str, option_2: str, path_1: str, path_2: str
    ) -> str | None:
        """Used by setters when there are two potential .json files to use.

        If you don't want to define an optional attribute for instantiation
        this function will make a random selection from two lists stored in
        .json files. Or you can pick from one of the lists by using option_1
        or option_2 as the attribute argument.

        Arguments
        ---------
        attribute: str or None
            Using None will pick randomly from both lists provided in the paths, or
            you can pass a string of option_1 or option_2 to make a random
            choice from the related path.
        option_1: str
            This should be the name of your first option.
        option_2: str
            This should be the name of your second option.
        path_1: str
            The path associated with option_1. Since all .json files are
            stored in /data/ the path should be:
                "[Class]/[attribute.json]"
            or
                "[Class]/[ChildClass]/[attribute.json]"
        path_2: str
            The path associated with option_2. Since all .json files are
            stored in /data/ the path should be:
                "[Class]/[attribute.json]"
            or
                "[Class]/[ChildClass]/[attribute.json]"
        """
        if attribute is None:
            attribute = choice(
                Generator.json_retriever(path_1) + Generator.json_retriever(path_2)
            )
        elif attribute.lower() == f"{option_1}":
            attribute = choice(Generator.json_retriever(path_1))
        elif attribute.lower() == f"{option_2}":
            attribute = choice(Generator.json_retriever(path_2))
        return attribute

    @staticmethod
    def second_roll_check(
        first_roll: str, triggers: list[str], forbidden: list[str], dataset: str
    ) -> str:
        """If the variable pulled for first_roll is in the triggers, it will
        start rolling for a second output from dataSet until it gets one that is
        not forbidden"""
        triggers_lower = [trigger_word.lower() for trigger_word in triggers]
        forbidden_lower = [forbidden_word.lower() for forbidden_word in forbidden]
        first_roll_lower = first_roll.lower()
        if first_roll_lower not in triggers_lower:
            return first_roll

        second_roll = choice(Generator.json_retriever(dataset))
        while second_roll.lower() in forbidden_lower:
            second_roll = choice(Generator.json_retriever(dataset))

        return first_roll + " " + second_roll
