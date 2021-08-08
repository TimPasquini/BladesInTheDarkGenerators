# doskvolMasterGenerator.py
# A menu interface capable of calling the individual Doskvol generators

import pyperclip

import doskvolBuildingGenerator as building
import doskvolDemonGenerator as demon
import doskvolGhostgenerator as ghost
import doskvolPeopleGenerator as npc
import doskvolStreetsGenerator as street
import doskvolCultGenerator as cult
import doskvolScoresGenerator as score


def main():
    while True:
        generator = input(
            """
Select generator:
[1] Create common NPC
[2] Create rare NPC
[3] Create street description
[4] Create common building desciption
[5] Create rare building description
[6] Create a demon
[7] Create a ghost
[8] Create a cult
[9] Create a score
[0] Quit

"""
        )
        if generator == "1":
            pyperclip.copy(npc.print_person("common"))

        elif generator == "2":
            pyperclip.copy(npc.print_person("rare"))

        elif generator == "3":
            pyperclip.copy(street.print_street())

        elif generator == "4":
            pyperclip.copy(building.print_building("common"))

        elif generator == "5":
            pyperclip.copy(building.print_building("rare"))

        elif generator == "6":
            random_demon = demon.build_demon()
            demon.print_demon(random_demon)

        elif generator == "7":
            random_ghost = ghost.build_ghost()
            ghost.print_ghost(random_ghost)

        elif generator == "8":
            random_cult = cult.build_cult()
            cult.print_cult(random_cult)

        elif generator == "9":
            random_score = score.build_score()
            score.print_score(random_score)
        elif generator == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
