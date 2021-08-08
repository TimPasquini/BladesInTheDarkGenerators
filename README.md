# BladesInTheDarkGenerators
A couple of generators I built for Blades in the Dark using the tables 
in the back of the book. The primary intent is speed of use and simplicity
of operation in order to minimize narrative disruptions caused by complex 
rolls across multiple tables. Ideally this makes your narrative seamless
during the occasions where a GM needs something on the fly. 

The generator outputs are loosely inspired from Dwarf Fortress's 
presentation when describing procedurally generated content. Due to tense, 
plurality, and other issues of language, sentences may sometimes still 
require a bit of creative interpretation. 

Feel free to make suggestions or report errors!

Stand-alone Instructions:
The executable has been removed due to it throwing anti-virus warnings. 
I used PyInstaller to compile and googling shows it's a common false-positive that
occurs with this compiler. I cannot verify what happens inside of PyInstaller
so out of an abundance of caution the .exe will be removed. If you really want it you 
can find it in older commits, but it is missing features and you use at your own risk. 
I will investigate a new way to compile the code to an executable, but for 
now you'll need python or you can see if one of the forks has a solution for you.

![generator_screenshot](https://user-images.githubusercontent.com/70915299/126913351-a50b0d98-91db-48f0-881f-d1063ef5a674.PNG)

Python instructions:
This project was built in python and can be run from the .py files in
the "src" folder if you have python installed. Double-click the 
doskvolMasterGenerator.py to launch. 

General operation info:

If you're running the Master Generator, just enter the number associated with the 
desired option to get an automatically generated description for that menu item. The
description will automatically be copied to your clipboard for easy pasting into
a VTT, chat, or your notes.

Each generator exists as individual module that can be run from a
terminal instance. Buildings and People require "common" or "rare" as
a terminal argument to work correctly.

For ease of modification of the various table contents, each table from 
the book is its own .json file which gets imported as a python list.

If the table options had more than one option for a given roll, they 
were split out so each is its own entry.

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

Cults:
Create a cult to a random forgotten god and assign a random religious practice to it using data on page 305.

Scores:
Create a random score using the data for pages 306 and 307.
