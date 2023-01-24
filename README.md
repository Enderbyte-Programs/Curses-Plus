# Curses Plus
Extension library to curses

## How To Install
Use ```pip3 install cursesplus```
on Linux

### SPECIAL INSTRUCTIONS FOR WINDOWS

For Windows you need to also install ```windows-curses``` or related program
to provide the basic curses functionality

## What's New?
### Patch 1.2.1

-Add new argument to ProgressBar.step()

-addmsgtolog (type bool) (default False)

-If set to True, will add "message" to log

-Only writes in normal colour. Use .appendlog() for custom colours

### Version 1.2
-Add Log to ProgressBar class

-Add WaitForKeyPress to ProgressBar class (default false)

-Log is default false

-Add to log with appendlog(text,colour)

-colour is curses.color-pair() value. NOTE: You must pass it through color_pair() before giving it to appendlog().


## Uses

curses-plus offers many utilities to make writing TUI applications easy. (TUI stands for Terminal User Interface)

### load_colours(grayscale=False)

load_colours() accept 0-1 args and initializes some colours. Usage of this function is required for optionmenu.
grayscale denotes if only grayscale should be used (grayscale can improve visibility on Windows)


*If I have more time I will finish this blasted documentation*