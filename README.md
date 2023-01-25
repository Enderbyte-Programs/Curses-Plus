# Curses Plus
Extension library to curses

## How To Install
Use ```pip3 install cursesplus```
on Linux

### SPECIAL INSTRUCTIONS FOR WINDOWS

For Windows you need to also install ```windows-curses``` or related program
to provide the basic curses functionality

## What's New?
## Version 1.3
-Add FileDialog.openfiledialog

-Accepts stdscr, filter, title, and directory

-filter example is ```[[filter glob (like *.py),filter name],["*Another filter*","Another filter"]]```

-Nested list

-Directory is what directory it should start on (default CWD)

-Title is the title that should be shown


## Uses

curses-plus offers many utilities to make writing TUI applications easy. (TUI stands for Terminal User Interface)

### load_colours(grayscale=False)

load_colours() accept 0-1 args and initializes some colours. Usage of this function is required for optionmenu.
grayscale denotes if only grayscale should be used (grayscale can improve visibility on Windows)


*If I have more time I will finish this blasted documentation*