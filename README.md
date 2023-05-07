# Curses Plus
Extension library to curses

## How To Install
Use ```pip3 install cursesplus```
on Linux or ```py -m pip install cursesplus```
on Windows

### SPECIAL INSTRUCTIONS FOR WINDOWS

For Windows you need to also install ```windows-curses``` or related program
to provide the basic curses functionality

### System requirements

**A computer running any of the following OSes:**

Microsoft Windows 7
Microsoft Windows 8
Microsoft Windows 8.1
Microsoft Windows 10
Microsoft Windows 11
Any modern distro of Linux that supports Python3

**Python Version 3.6 or newer**

## What's New?

### Version 2.0.5

Fix small bug in Manjaro Konsole

### Version 2.0.4

More features added to filedialog

### Version 2.0: Incompatible api changes

-askyesno now MUST be messagebox.askyesno
-Rewrite colour system. load_colours() is now nonexistent.
-Now use set_colour(background,foreground). A set of colour constants are defined in the cp class.

## Uses

curses-plus offers many utilities to make writing TUI applications easy. (TUI stands for Terminal User Interface)