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


# Building Data

BUILDING_RARE_PURPOSES = DATA_DIRECTORY / "Buildings/rare_use.json"
BUILDING_COMMON_PURPOSES = DATA_DIRECTORY / "Buildings/common_use.json"
BUILDING_MATERIALS = DATA_DIRECTORY / "Buildings/material.json"
BUILDING_EXTERIORS = DATA_DIRECTORY / "Buildings/exterior_details.json"
BUILDING_INTERIORS = DATA_DIRECTORY / "Buildings/interior_details.json"


# Cult Data
FORGOTTEN_GODS = DATA_DIRECTORY / "Cults/forgotten_gods.json"
CULT_PRACTICES = DATA_DIRECTORY / "Cults/cult_practices.json"

# Demon Data
DEMON_NAMES = DATA_DIRECTORY / "Demons/demon_names.json"
DEMON_FEATURES = DATA_DIRECTORY / "Demons/demon_features.json"
DEMON_ASPECTS = DATA_DIRECTORY / "Demons/demonic_aspect.json"
DEMON_AFFINITYS = DATA_DIRECTORY / "Demons/demonic_affinity.json"
DEMON_DESIRES = DATA_DIRECTORY / "Demons/demon_desire.json"

# Ghost Data
GHOST_TRAITS = DATA_DIRECTORY / "Ghosts/ghost_traits.json"
GHOST_EFFECTS = DATA_DIRECTORY / "Ghosts/ghostly_effect.json"

# People Data
RARE_PROFESSIONS = DATA_DIRECTORY / "People/rare_profession.json"
COMMON_PROFESSIONS = DATA_DIRECTORY / "People/common_profession.json"
GENDERS = DATA_DIRECTORY / "People/gender.json"
APPEARANCES = DATA_DIRECTORY / "People/appearance.json"
GOALS = DATA_DIRECTORY / "People/goals.json"
METHODS = DATA_DIRECTORY / "People/methods.json"
STYLES = DATA_DIRECTORY / "People/style.json"
TRAITS = DATA_DIRECTORY / "People/traits.json"
INTERESTS = DATA_DIRECTORY / "People/interests.json"
QUIRKS = DATA_DIRECTORY / "People/quirks.json"
FIRST_NAMES = DATA_DIRECTORY / "People/first_names.json"
FAMILY_NAMES = DATA_DIRECTORY / "People/family_names.json"
ALIASES = DATA_DIRECTORY / "People/aliases.json"
HERITAGES = DATA_DIRECTORY / "People/heritage.json"

# Leviathan Data
LEVIATHAN_BANAL_ACTIVITIES = DATA_DIRECTORY / "Leviathan/banal_activity.json"
LEVIATHAN_SURREAL_ACTIVITIES = DATA_DIRECTORY / "Leviathan/surreal_activity.json"
LEVIATHAN_NAMES = DATA_DIRECTORY / "Leviathan/leviathan_names.json"
LEVIATHAN_EPITHETS = DATA_DIRECTORY / "Leviathan/epithet.json"
LEVIATHAN_SHAPES = DATA_DIRECTORY / "Leviathan/shapes.json"
LEVIATHAN_DEMONIC_TRAITS = DATA_DIRECTORY / "Leviathan/leviathan_demon_traits.json"
LEVIATHAN_TREASURES = DATA_DIRECTORY / "Leviathan/leviathan_treasures.json"
LEVIATHAN_SPAWN_FORMS = DATA_DIRECTORY / "Leviathan/leviathan_spawn.json"

# Score Data
SCORE_CLIENTS_TARGETS = DATA_DIRECTORY / "Scores/client_target.json"
SCORE_JOBS = DATA_DIRECTORY / "Scores/score_type.json"
SCORE_TWISTS = DATA_DIRECTORY / "Scores/complication.json"
SCORE_CONNECTIONS = DATA_DIRECTORY / "Scores/connection.json"
SCORE_FACTIONS = DATA_DIRECTORY / "Scores/factions.json"

# Street Data
STREET_MOODS = DATA_DIRECTORY / "Streets/moods.json"
STREET_SIGHTS = DATA_DIRECTORY / "Streets/sights.json"
STREET_SOUNDS = DATA_DIRECTORY / "Streets/sounds.json"
STREET_SMELLS = DATA_DIRECTORY / "Streets/smells.json"
STREET_USES = DATA_DIRECTORY / "Streets/use.json"
STREET_INFASTRUCTURE_TYPES = DATA_DIRECTORY / "Streets/infastructure_type.json"
STREET_DETAILS = DATA_DIRECTORY / "Streets/details.json"
