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
The easiest way to use these generators is via it's discord bot implementation, [Sparkwright](https://discord.com/oauth2/authorize?client_id=896105913960788029&permissions=59456&scope=bot). Type "!help" to get started. 
There are several forks that use their own implementations like a web interface 
or .exe with gui. If you want to use this program as-is you'll need python. See
instructions below. 

![generator_screenshot](https://github.com/TimPasquini/BladesInTheDarkGenerators/blob/e4f40e531f6341412f7e761d7e853b4066cb4349/generator_screenshot.PNG)

Python instructions:
This project was built in python and can be run from the .py files in
the "src" folder if you have python installed. Just double-click the 
doskvolMasterGenerator.py file in the "src" folder to launch it. 

General Operation Info:

If you're running the Master Generator, just enter the number associated with the 
desired option to get an automatically generated description for that menu item. 
If you have pyperclip installed, the description will automatically be copied 
to your clipboard for easy pasting into a VTT, chat, or your notes. The Master
Generator will also print your generated descriptions to a text file log.

Each generator exists as individual module that can be run from a
terminal instance. Several of them require arguements to run correctly.

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

Leviathans:
Uses the Leviathan Song supplement, [available free here](https://bladesinthedark.com/blades-supplements), to create leviathans and spawn.
Requires the arguments "banal" or "surreal" to decide the leviathan's initial activity.