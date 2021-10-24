# doskvolMasterGenerator.py
# A menu interface capable of calling the individual Doskvol generators

try:
    import pyperclip
    clipboard_support = True
except ImportError:
    clipboard_support = False

import doskvolBuildingGenerator as building
import doskvolDemonGenerator as demon
import doskvolGhostgenerator as ghost
import doskvolPeopleGenerator as npc
import doskvolStreetsGenerator as street
import doskvolCultGenerator as cult
import doskvolScoresGenerator as score
import utils


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

        if generator == "0":
            break

        elif generator == "1":
            common_person = npc.build_person()
            description = npc.print_person("common", common_person)

        elif generator == "2":
            rare_person = npc.build_person()
            description = npc.print_person("rare", rare_person)

        elif generator == "3":
            random_street = street.build_street()
            description = street.print_street(random_street)

        elif generator == "4":
            common_building = building.build_building()
            description = building.print_building("common", common_building)

        elif generator == "5":
            rare_building = building.build_building()
            description = building.print_building("rare", rare_building)

        elif generator == "6":
            random_demon = demon.build_demon()
            description = demon.print_demon(random_demon)

        elif generator == "7":
            random_ghost = ghost.build_ghost()
            description = ghost.print_ghost(random_ghost)

        elif generator == "8":
            random_cult = cult.build_cult()
            description = cult.print_cult(random_cult)

        elif generator == "9":
            random_score = score.build_score()
            description = score.print_score(random_score)

        else:
            print("Invalid choice. Please try again.")
            continue

        print(description)
        if clipboard_support:
            pyperclip.copy(description)
        utils.history_log(description)


if __name__ == "__main__":
    main()
