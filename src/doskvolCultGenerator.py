# doskvolCultGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a cult to
# Forgotten God and assign a random practice to their cultists.

from utils import rc, json_retreiver

def print_cult():
    """This function will return a description of a randomly generated cult
    it will select a random Forgotten God for the cult and assign them
    a random practice."""
    output= f"""
        This is the cult of {rc(god)}. Their cultists follow an
        edict of {rc(practice)}
        """
    print(output)
    return output

god = json_retreiver("Cults/forgotten_gods.json")
practice = json_retreiver("Cults/cult_practices.json")

if __name__ == '__main__':
    print_cult()