# StepZone
 Terminal-based rhythm game written in Python 3.9

StepZone is a rhythm game written in Python 3.9 that runs entirely in your terminal.

## Libraries required
* colorama
* keyboard

## Running the game
### From source
* Download the game's source code.
* Please make sure you have the latest version of Python, the colorama library and the keyboard library.
#### Windows
* Open Windows Terminal (not CMD) or PowerShell (using CMD introduces visual bugs (and by that I mean printXY() doesn't work as intended)).
* Type `py main.py`, press Enter and you're golden!
#### macOS/Linux
* Open your terminal of choice.
* Type `py main.py`, press Enter and you're in the game!
### From built executable (Windows ONLY)
* Open Windows Terminal (not CMD) or PowerShell.
* Type `main`, press Enter and enjoy music!

## Game
### Controls and gameplay
The game controls are currently fixed. This will be changed in the future.<br>
To hit the notes (●), you must hit D, F, J or K when a note enters the corresponding receptor.<br>
(Not implemented yet) When a mine (◇) passes on a receptor, mace sure your finger is not on the corresponding key. Hitting a mine will drain your (currently non-existent) life bar.