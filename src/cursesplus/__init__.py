"""
# Curses Plus
Curses Plus is an extension to the curses module that provides some useful featues. This library will be distributed as part of many Enderbyte Programs software products
(c) 2022-2023 Enderbyte Programs, no rights reserved

Source code at https://github.com/Enderbyte-Programs/Curses-Plus
Available on the Python Package Index

## Sub-Packages List

cursesplus.tuibase         Auto imported. Base utilties

cursesplus.filedialog       Advanced dialogues for file selection

cursesplus.messagebox       Assorted messageboxes

cursesplus.transitions      Animated transitions

cursesplus.widgets          Auto imported. Contains Widget classes for drawing UI

cursesplus.cp               Old-style utilities. Imported as classic namespace

NOTICE! CP UTILITIES ARE COMPLETELY INCOMPATIBLE WITH TUIBASE. TO USE THEM, CALL your BaseWindows.screen for the stdscr argument.
"""

__version__ = "3.1"
__author__ = "Enderbyte Programs"
__package__ = "cursesplus"

from .tuibase import *
from . import transitions
from . import filedialog
from .widgets import *
from . import cp as classic
from . import messagebox