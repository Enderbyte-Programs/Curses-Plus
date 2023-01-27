# Curses Plus
Extension library to curses

## How To Install
Use ```pip3 install cursesplus```
on Linux or ```py -m pip install cursesplus```
on Windows

### SPECIAL INSTRUCTIONS FOR WINDOWS

For Windows you need to also install ```windows-curses``` or related program
to provide the basic curses functionality

## What's New?
## Version 1.4
-Clear up some package style issues. __cptest.py is now top-level.

-Move Fileobj(), parse_size() to .filedialog

-Remove bad dependancies from cursesplus.cp

-Add openfilesdialog()

-Like openfiledialog() but you can choose multiple files

-Has more keybinds

-Add return types for all public filedialog() functions

## Uses

curses-plus offers many utilities to make writing TUI applications easy. (TUI stands for Terminal User Interface)

### load_colours(grayscale=False)

load_colours() accept 0-1 args and initializes some colours. Usage of this function is required for optionmenu.
grayscale denotes if only grayscale should be used (grayscale can improve visibility on Windows)


*If I have more time I will finish this blasted documentation*