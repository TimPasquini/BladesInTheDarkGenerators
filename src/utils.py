import json
import random


def json_retreiver(json_filename):
    """Call this from a variable with a filename string to populate
    with json content"""
    filename = json_filename
    with open(filename) as f:
        return json.load(f)


def rc(variable):
    """rc = random choice. Picks a random item from the list and returns
    it. This is mostly to shorten up the variables in the print command"""
    return random.choice(variable)


def history_log(output):
    """Writes each generator call to an text file so that it's not lost
    when the program is closed or crashes."""
    filename = "history.txt"
    with open(filename, "a") as f:
        f.write(output)
        f.write("\n\n")
