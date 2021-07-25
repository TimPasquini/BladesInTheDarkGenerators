# BladesInTheDarkGenerators
A couple of generators I built for Blades in the Dark using the tables 
in the back of the book. 

Double-click the doskvolMasterGenerator.py to launch. Enter the number
associated with the desired option to get an automatically generated
description.


Each generator exists as individual module that can be run from a
terminal instance. Buildings and People require "common" or "rare" as
a terminal argument to work correctly.

For ease of modification of the various table contents, each table from 
the book is it's own .json file which gets imported as a python list.

If the table options had more than one option for a given roll, they 
were split out so each is it's own entry.

Due to inconsistency on the tables, sometimes the output is imperfect in
terms of case/tense/pronoun/etc.

Streets:
Get a random street description using the information from page 300 of 
the Blades in the Dark sourcebook.

Buildings:
Get a random building description using the information from page 301. 
Use the arguments "rare" or "common" in the terminal to decide which 
table to roll from.

People:
Get a random NPC from the data on pages 302 and 303. Use the arguments
"rare" or "common" in the terminal to decide which profession table to 
roll from.

Demons:
Creates a random demon out of the data on page 304. 

Ghosts:
Creates a random ghost using the ghost tables on page 304. 
Also uses the names/aliases from page 303 to give a name to the ghost.