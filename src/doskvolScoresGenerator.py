# doskvolScoresGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a random
# score.

from utils import rc, json_retreiver

def print_score(score_dict):
    """ This will print a score. Scores can have re-roll elements and a
    varying number of elements. This will probably need to receive a
    dictionary as in input to check for certain conditions and then direct
    to the correct script"""
    print(score_dict)

def build_score():
    """ This will replace the regular method of polling the .json lists
    so that you have them in a data structure. Call the function by assigning
    to a variable that gets passed to print_score()"""
    score_dict = {}
    score_dict['client'] = 
    score_dict['target'] = 
    score_dict['job'] = 
    score_dict['twist']
    score_dict['connection'] =
    score_dict['faction'] =
    return score_dict

if __name__ == '__main__':
    new_score = build_score()
    print_score(new_score)
