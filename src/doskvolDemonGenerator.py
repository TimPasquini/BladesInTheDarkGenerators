# doskvolDemonGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random demon.

from utils import rc, json_retreiver


def print_demon():
    """This will print text describing a new demon"""
    output = f"""
    Tremble at the sight of {rc(demon_name)}!
    Behold, {rc(demon_features)} and {rc(demon_features)}.
    This {rc(demonic_affinity)} demon has a {rc(demonic_aspect)} aspect.
    This demon desires {rc(demon_desire)} above all else!
    """
    print(output)
    return output


demon_name = json_retreiver("Demons/demon_names.json")
demon_features = json_retreiver("Demons/demon_features.json")
demonic_aspect = json_retreiver("Demons/demonic_aspect.json")
demonic_affinity = json_retreiver("Demons/demonic_affinity.json")
demon_desire = json_retreiver("Demons/demon_desire.json")

if __name__ == "__main__":
    print_demon()
