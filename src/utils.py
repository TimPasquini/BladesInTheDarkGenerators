"""
General utility functions used by the generators.

...

Functions
---------
json_retreiver: str
    Used to assign the contents of a .json to a variable
history_log: str
    writes any output string to an external text document
simple_attribute_setter: str or None
    used by setters to pull from .json if None is passed
two_choice_attribute_setter: string or None
    used by setters when there are two potential .json files to use
"""

import json

from random import choice


def json_retreiver(json_filepath: str):
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


def history_log(output):
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
        attribute = choice(json_retreiver(f"../data/{path}"))
    return attribute


def two_choice_attribute_setter(
    attribute: str | None, option_1: str, option_2: str, path_1: str, path_2: str
) -> str | None:
    """Used by setters when there are two potential .json files to use.

    If you don't want to define an optional attribute for instationation
    this function will make a random selection from two lists stored in
    .json files. Or you can pick from one of the lists by using option_1
    or option_2 as the attribute argument.

    Arguments
    ---------
    attribute: str or None
        None will pick randomly from both lists provided in the paths or
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
            json_retreiver(f"../data/{path_1}") + json_retreiver(f"../data/{path_2}")
        )
    elif attribute.lower() == f"{option_1.lower()}":
        attribute = choice(json_retreiver(f"../data/{path_1}"))
    elif attribute.lower() == f"{option_2.lower()}":
        attribute = choice(json_retreiver(f"../data/{path_2}"))
    return attribute
