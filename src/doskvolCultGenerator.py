# doskvolCultGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a cult to
# Forgotten God and assign a random practice to their cultists.

from utils import rc, json_retreiver


def print_cult(cult_dict):
    """This function will return a description of a randomly generated cult
    it will select a random Forgotten God for the cult and assign them
    a random practice."""
    output = f"""
This is the cult of {cult_dict["god"].title()}. 
Their cultists follow an edict of:
    {cult_dict["practice"].capitalize()}
        """
    print(output)
    return output


def build_cult():
    """Call the function by assigning to a variable that gets passed to
    print_cult(). This function pulls lists from the .json files and then
    selects a random entry from that, then assigns to a dict. You need to
    re-call this function if you want a new set of random variables."""
    cult_dict = {}
    cult_dict["god"] = rc(json_retreiver("Cults/forgotten_gods.json"))
    cult_dict["practice"] = rc(json_retreiver("Cults/cult_practices.json"))
    return cult_dict


if __name__ == "__main__":
    random_cult = build_cult()
    print_cult(random_cult)
