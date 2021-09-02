# doskvolDemonGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random demon.

from utils import rc, json_retreiver


def print_demon(demon_dict):
    """This will print text describing a new demon"""
    output = f"""
Tremble at the sight of {demon_dict["name"].capitalize()}!
Behold, {demon_dict["feature_1"].lower()} and {demon_dict["feature_2"].lower()}.
This {demon_dict["affinity"].lower()} demon has a {demon_dict["aspect"].lower()} aspect.
This demon desires {demon_dict["desire"].lower()} above all else!
    """
    print(output)
    return output


def build_demon():
    """Call the function by assigning to a variable that gets passed to
    print_demon(). This function pulls lists from the .json files and then
    selects a random entry from that, then assigns to a dict. You need to
    re-call this function if you want a new set of random variables."""
    demon_dict = {}
    demon_dict["name"] = rc(json_retreiver("Demons/demon_names.json"))
    demon_dict["feature_1"] = rc(json_retreiver("Demons/demon_features.json"))
    demon_dict["feature_2"] = rc(json_retreiver("Demons/demon_features.json"))
    demon_dict["aspect"] = rc(json_retreiver("Demons/demonic_aspect.json"))
    demon_dict["affinity"] = rc(json_retreiver("Demons/demonic_affinity.json"))
    demon_dict["desire"] = rc(json_retreiver("Demons/demon_desire.json"))
    return demon_dict


if __name__ == "__main__":
    random_demon = build_demon()
    print_demon(random_demon)
