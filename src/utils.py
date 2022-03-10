import json


def json_retreiver(json_filename):
    """Call this from a variable with a filename string to populate
    with json content"""
    filename = json_filename
    with open(filename) as f:
        return json.load(f)


def history_log(output):
    """Writes each generator call to an text file so that it's not lost
    when the program is closed or crashes."""
    filename = "history.txt"
    with open(filename, "a") as f:
        f.write(output)
        f.write("\n\n")
