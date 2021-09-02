# doskvolScoresGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a random
# score.

from utils import rc, json_retreiver


def print_score(score_dict):
    """This will print a score from a score_dict. Scores can involve ghosts
    which requires a re-roll. The _ghostbuster() helper runs a check to handle
    this issue."""
    score_dict = _ghostbuster(score_dict)
    if score_dict.get("c_ghost", False) and score_dict.get("t_ghost", False):
        output = f"""
A {score_dict['client']} a {score_dict['c_ghost']} wants the crew to {score_dict['job']} a {score_dict['target']} a {score_dict['t_ghost']}.
It's more complex because...
    {score_dict['twist']}. 
A {score_dict['connection']} has some further insights into the bigger picture, 
    but {score_dict['faction']} are also involved.
        """
        print(output)
        return output
    elif score_dict.get("c_ghost", False):
        output = f"""
A {score_dict['client']} a {score_dict['c_ghost']} wants the crew to {score_dict['job']} a {score_dict['target']}.
It's more complex because...
    {score_dict['twist']}.
A {score_dict['connection']} has some further insights into the bigger picture, 
    but {score_dict['faction']} are also involved.
        """
        print(output)
        return output
    elif score_dict.get("t_ghost", False):
        output = f"""
A {score_dict['client']} wants the crew to {score_dict['job']} a {score_dict['target']} a {score_dict['t_ghost']}.
It's more complex because...
    {score_dict['twist']}. 
A {score_dict['connection']} has some further insights into the bigger picture, 
    but {score_dict['faction']} are also involved.
        """
        print(output)
        return output
    else:
        output = f"""
A {score_dict['client']} wants the crew to {score_dict['job']} a {score_dict['target']}.
It's more complex because...
    {score_dict['twist']}. 
A {score_dict['connection']} has some further insights into the bigger picture, 
    but {score_dict['faction']} are also involved.
        """
        print(output)
        return output


def _ghostbuster(score_dict):
    """This function checks for ghosts in the score_dict and will assign them
    a profession/role that they held in life. It will reroll if it pulls 'Ghost of'
    a second time"""
    if score_dict["client"] and score_dict["target"] == "Ghost of":
        score_dict["c_ghost"] = rc(json_retreiver("Scores/client_target.json"))
        score_dict["t_ghost"] = rc(json_retreiver("Scores/client_target.json"))
        while (
            score_dict["c_ghost"] == "Ghost of" or score_dict["t_ghost"] == "Ghost of"
        ):
            score_dict["c_ghost"] = rc(json_retreiver("Scores/client_target.json"))
            score_dict["t_ghost"] = rc(json_retreiver("Scores/client_target.json"))
    elif score_dict["client"] == "Ghost of":
        score_dict["c_ghost"] = rc(json_retreiver("Scores/client_target.json"))
        while score_dict["c_ghost"] == "Ghost of":
            score_dict["c_ghost"] = rc(json_retreiver("Scores/client_target.json"))
    elif score_dict["target"] == "Ghost of":
        score_dict["t_ghost"] = rc(json_retreiver("Scores/client_target.json"))
        while score_dict["t_ghost"] == "Ghost of":
            score_dict["t_ghost"] = rc(json_retreiver("Scores/client_target.json"))
    return score_dict


def build_score():
    """Call the function by assigning to a variable that gets passed
    to print_score(). This function is what pulls lists from the .json files
    and then selects a random entry, then assigns it to a dict. You need to
    re-call this function if you want a new set of random variables."""
    score_dict = {}
    score_dict["client"] = rc(json_retreiver("Scores/client_target.json"))
    score_dict["target"] = rc(json_retreiver("Scores/client_target.json"))
    score_dict["job"] = rc(json_retreiver("Scores/score_type.json"))
    score_dict["twist"] = rc(json_retreiver("Scores/complication.json"))
    score_dict["connection"] = rc(json_retreiver("Scores/connection.json"))
    score_dict["faction"] = rc(json_retreiver("Scores/factions.json"))
    return score_dict


if __name__ == "__main__":
    new_score = build_score()
    print_score(new_score)
