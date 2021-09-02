# doskvolStreetsGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random city street.

from utils import rc, json_retreiver


def print_street(street_dict):
    """This will print text describing a random street"""
    output = f"""
This {street_dict["moods"]} {street_dict["infastructure_type"]} is primarily used for {street_dict["use"]} purposes.
(A/An) {street_dict["sights"]} catch(es) your eye. 
You hear {street_dict["sounds"]} and smell {street_dict["smells"]} on the air. 
You can't help but notice {street_dict["details_1"]} and {street_dict["details_2"]}."""
    print(output)
    return output


def build_street():
    """Call the function by assigning to a variable that gets passed to
    print_street(). This function pulls lists from the .json files and then
    selects a random entry from that, then assigns to a dict. You need to
    re-call this function if you want a new set of random variables."""
    street_dict = {}
    street_dict["moods"] = rc(json_retreiver("Streets/moods.json"))
    street_dict["sights"] = rc(json_retreiver("Streets/sights.json"))
    street_dict["sounds"] = rc(json_retreiver("Streets/sounds.json"))
    street_dict["smells"] = rc(json_retreiver("Streets/smells.json"))
    street_dict["use"] = rc(json_retreiver("Streets/use.json"))
    street_dict["infastructure_type"] = rc(
        json_retreiver("Streets/infastructure_type.json")
    )
    street_dict["details_1"] = rc(json_retreiver("Streets/details.json"))
    street_dict["details_2"] = rc(json_retreiver("Streets/details.json"))
    return street_dict


if __name__ == "__main__":
    print_street()
