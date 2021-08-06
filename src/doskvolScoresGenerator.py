# doskvolScoresGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a random
# score.

from utils import rc, json_retreiver

def print_score(score_dict):
    """ This will print a score. Scores can have re-roll elements and a
    varying number of elements. This will probably need to receive a
    dictionary as in input to check for certain conditions and then direct
    to the correct script"""
    if score_dict['client'] == 'Ghost of':
        score_dict['ghost'] = rc(json_retreiver('Scores/client_target.json'))
        output = f"""
        A {score_dict['client']} a {score_dict['ghost']} wants the crew to {score_dict['job']} a {score_dict['target']}.
        It's more complex because {score_dict['twist']}. A {score_dict['connection']} has
        some further insights into the bigger picture, but {score_dict['faction']} are also involved.
        """
        print(output)
        return output
    elif score_dict['target'] == 'Ghost of':
        score_dict['ghost'] = rc(json_retreiver('Scores/client_target.json'))
        output = f"""
        A {score_dict['client']} wants the crew to {score_dict['job']} a {score_dict['target']} a {score_dict['ghost']}.
        It's more complex because {score_dict['twist']}. A {score_dict['connection']} has
        some further insights into the bigger picture, but {score_dict['faction']} are also involved.
        """
        print(output)
        return output
    else:
        output = f"""
        A {score_dict['client']} wants the crew to {score_dict['job']} a {score_dict['target']}.
        It's more complex because {score_dict['twist']}. A {score_dict['connection']} has
        some further insights into the bigger picture, but {score_dict['faction']} are also involved.
        """
        print(output)
        return output

def build_score():
    """ This will replace the regular method of polling the .json lists
    so that you have them in a data structure. Call the function by assigning
    to a variable that gets passed to print_score()"""
    score_dict = {}
    score_dict['client'] = rc(json_retreiver("Scores/client_target.json"))
    score_dict['target'] = rc(json_retreiver("Scores/client_target.json"))
    score_dict['job'] = rc(json_retreiver("Scores/score_type.json"))
    score_dict['twist'] = rc(json_retreiver("Scores/complication.json"))
    score_dict['connection'] = rc(json_retreiver("Scores/connection.json"))
    score_dict['faction'] = rc(json_retreiver("Scores/factions.json"))
    return score_dict

if __name__ == '__main__':
    new_score = build_score()
    print_score(new_score)
