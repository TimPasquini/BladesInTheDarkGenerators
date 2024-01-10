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

    # define dictionary mapping inputs to choices
    # instantiation occurs later, lambda blocks instantiation of objects that need arguments
    generators = {
        "1": lambda: people.Person("common"),
        "2": lambda: people.Person("rare"),
        "3": streets.Street,
        "4": lambda: buildings.Building("common"),
        "5": lambda: buildings.Building("rare"),
        "6": demons.Demon,
        "7": ghosts.Ghost,
        "8": cults.Cult,
        "9": scores.Score,
        "10": lambda: leviathans.Leviathan("banal"),
        "11": lambda: leviathans.Leviathan("surreal"),
        "12": leviathans.LeviathanSpawn,
    }

    while True:
        chosen_generator = input(
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

        if chosen_generator == "0":
            break

        try:
            entity = generators[
                chosen_generator
            ]()  # this is where we instantiate the object
            description = entity.describe()
            entity.history_log(description)
            print(description)
            if clipboard_support:
                pyperclip.copy(description)
        except KeyError:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
