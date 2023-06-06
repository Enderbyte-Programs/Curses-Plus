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

### Patch 2.3.5:

-Add ability to not include empty newlines in multiline text input

### Version 2.3: New Input

-Rewrite cursesinput function

-Remains backwards-compatible

### Version 2.0: Incompatible api changes

-askyesno now MUST be messagebox.askyesno

-Rewrite colour system. load_colours() is now nonexistent.

-Now use set_colour(background,foreground). A set of colour constants are defined in the cp class.

## Uses

curses-plus offers many utilities to make writing TUI applications easy. (TUI stands for Terminal User Interface)

## Documentation

TODO