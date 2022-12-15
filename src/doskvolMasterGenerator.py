# doskvolMasterGenerator.py
# A menu interface capable of calling the individual Doskvol generators

try:
    import pyperclip  # type: ignore

    clipboard_support = True
except ImportError:
    clipboard_support = False

import buildings
import demons
import ghosts
import leviathans
import people
import streets
import cults
import scores


def main():
    while True:
        generator = input(
            """
Select generator:
[1]  Create common NPC
[2]  Create rare NPC
[3]  Create street description
[4]  Create common building description
[5]  Create rare building description
[6]  Create a demon
[7]  Create a ghost
[8]  Create a cult
[9]  Create a score
[10] Create a leviathan doing banal activity
[11] Create a leviathan doing surreal activity
[12] Create a leviathan spawn
[0] Quit

"""
        )

        if generator == "0":
            break

        elif generator == "1":
            common_person = people.Person("common")
            description = common_person.describe()
            common_person.history_log(description)

        elif generator == "2":
            rare_person = people.Person("rare")
            description = rare_person.describe()
            rare_person.history_log(description)

        elif generator == "3":
            random_street = streets.Street()
            description = random_street.describe()
            random_street.history_log(description)

        elif generator == "4":
            common_building = buildings.Building("common")
            description = common_building.describe()
            common_building.history_log(description)

        elif generator == "5":
            rare_building = buildings.Building("rare")
            description = rare_building.describe()
            rare_building.history_log(description)

        elif generator == "6":
            random_demon = demons.Demon()
            description = random_demon.describe()
            random_demon.history_log(description)

        elif generator == "7":
            random_ghost = ghosts.Ghost()
            description = random_ghost.describe()
            random_ghost.history_log(description)

        elif generator == "8":
            random_cult = cults.Cult()
            description = random_cult.describe()
            random_cult.history_log(description)

        elif generator == "9":
            random_score = scores.Score()
            description = random_score.describe()
            random_score.history_log(description)

        elif generator == "10":
            random_leviathan = leviathans.Leviathan("banal")
            description = random_leviathan.describe()
            random_leviathan.history_log(description)

        elif generator == "11":
            random_leviathan = leviathans.Leviathan("surreal")
            description = random_leviathan.describe()
            random_leviathan.history_log(description)

        elif generator == "12":
            random_spawn = leviathans.LeviathanSpawn()
            description = random_spawn.describe()
            random_spawn.history_log(description)

        else:
            print("Invalid choice. Please try again.")
            continue

        print(description)
        if clipboard_support:
            pyperclip.copy(description)


if __name__ == "__main__":
    main()
