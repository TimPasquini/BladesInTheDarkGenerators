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
            common_person = npc.build_person()
            pyperclip.copy(npc.print_person("common", common_person))

        elif generator == "2":
            rare_person = npc.build_person()
            pyperclip.copy(npc.print_person("rare", rare_person))

        elif generator == "3":
            random_street = street.build_street()
            pyperclip.copy(street.print_street(random_street))

        elif generator == "4":
            common_building = building.build_building()
            pyperclip.copy(building.print_building("common", common_building))

        elif generator == "5":
            rare_building = building.build_building()
            pyperclip.copy(building.print_building("rare", rare_building))

        elif generator == "6":
            random_demon = demon.build_demon()
            pyperclip.copy(demon.print_demon(random_demon))

        elif generator == "7":
            random_ghost = ghost.build_ghost()
            pyperclip.copy(ghost.print_ghost(random_ghost))

        elif generator == "8":
            random_cult = cult.build_cult()
            pyperclip.copy(cult.print_cult(random_cult))

        elif generator == "9":
            random_score = score.build_score()
            pyperclip.copy(score.print_score(random_score))

        elif generator == "0":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
