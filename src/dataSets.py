# dataSets.py
"""
This file contains variables that reference the filepath of every data set in
the project's data folder. These should be imported using * and treated as
constants.
"""

from pathlib import Path


# Establish a path to this file
PATH_TO_DATASETS_FILE = Path(__file__)

# Path to SRC directory
SRC_DIRECTORY = PATH_TO_DATASETS_FILE.parent

# Path to project Root
PROJECT_ROOT = SRC_DIRECTORY.parent

# Path to data folder
DATA_DIRECTORY = PROJECT_ROOT / "data"


BUILDING = {
    "RARE_PURPOSES": DATA_DIRECTORY / "Buildings/rare_use.json",
    "COMMON_PURPOSES": DATA_DIRECTORY / "Buildings/common_use.json",
    "MATERIALS": DATA_DIRECTORY / "Buildings/material.json",
    "EXTERIORS": DATA_DIRECTORY / "Buildings/exterior_details.json",
    "INTERIORS": DATA_DIRECTORY / "Buildings/interior_details.json"
    }

CULT = {
    "FORGOTTEN_GODS": DATA_DIRECTORY / "Cults/forgotten_gods.json",
    "PRACTICES": DATA_DIRECTORY / "Cults/cult_practices.json"
    }

DEMON = {
    "NAMES": DATA_DIRECTORY / "Demons/demon_names.json",
    "FEATURES": DATA_DIRECTORY / "Demons/demon_features.json",
    "ASPECTS": DATA_DIRECTORY / "Demons/demonic_aspect.json",
    "AFFINITIES": DATA_DIRECTORY / "Demons/demonic_affinity.json",
    "DESIRES": DATA_DIRECTORY / "Demons/demon_desire.json",
    }

GHOST = {
    "TRAITS": DATA_DIRECTORY / "Ghosts/ghost_traits.json",
    "EFFECTS": DATA_DIRECTORY / "Ghosts/ghostly_effect.json",
    }

PEOPLE = {
    "RARE_PROFESSIONS": DATA_DIRECTORY / "People/rare_profession.json",
    "COMMON_PROFESSIONS": DATA_DIRECTORY / "People/common_profession.json",
    "GENDERS": DATA_DIRECTORY / "People/gender.json",
    "APPEARANCES": DATA_DIRECTORY / "People/appearance.json",
    "GOALS": DATA_DIRECTORY / "People/goals.json",
    "METHODS": DATA_DIRECTORY / "People/methods.json",
    "STYLES": DATA_DIRECTORY / "People/style.json",
    "TRAITS": DATA_DIRECTORY / "People/traits.json",
    "INTERESTS": DATA_DIRECTORY / "People/interests.json",
    "QUIRKS": DATA_DIRECTORY / "People/quirks.json",
    "FIRST_NAMES": DATA_DIRECTORY / "People/first_names.json",
    "FAMILY_NAMES": DATA_DIRECTORY / "People/family_names.json",
    "ALIASES": DATA_DIRECTORY / "People/aliases.json",
    "HERITAGES": DATA_DIRECTORY / "People/heritage.json",
    }

LEVIATHAN = {
    "BANAL_ACTIVITIES": DATA_DIRECTORY / "Leviathan/banal_activity.json",
    "SURREAL_ACTIVITIES": DATA_DIRECTORY / "Leviathan/surreal_activity.json",
    "NAMES": DATA_DIRECTORY / "Leviathan/leviathan_names.json",
    "EPITHETS": DATA_DIRECTORY / "Leviathan/epithet.json",
    "SHAPES": DATA_DIRECTORY / "Leviathan/shapes.json",
    "DEMONIC_TRAITS": DATA_DIRECTORY / "Leviathan/leviathan_demon_traits.json",
    "TREASURES": DATA_DIRECTORY / "Leviathan/leviathan_treasures.json",
    "SPAWN_FORMS": DATA_DIRECTORY / "Leviathan/leviathan_spawn.json",
    }

SCORE = {
    "CLIENTS_TARGETS": DATA_DIRECTORY / "Scores/client_target.json",
    "JOBS": DATA_DIRECTORY / "Scores/score_type.json",
    "TWISTS": DATA_DIRECTORY / "Scores/complication.json",
    "CONNECTIONS": DATA_DIRECTORY / "Scores/connection.json",
    "FACTIONS": DATA_DIRECTORY / "Scores/factions.json",
    }
STREET = {
    "MOODS": DATA_DIRECTORY / "Streets/moods.json",
    "SIGHTS": DATA_DIRECTORY / "Streets/sights.json",
    "SOUNDS": DATA_DIRECTORY / "Streets/sounds.json",
    "SMELLS": DATA_DIRECTORY / "Streets/smells.json",
    "USES": DATA_DIRECTORY / "Streets/use.json",
    "INFRASTRUCTURE_TYPES": DATA_DIRECTORY / "Streets/infrastructure_type.json",
    "DETAILS": DATA_DIRECTORY / "Streets/details.json",
    }
