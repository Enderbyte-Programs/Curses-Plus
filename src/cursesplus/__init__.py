"""
# Curses Plus
Curses Plus is an extension to the curses module that provides some useful featues. This library will be distributed as part of many Enderbyte Programs software products
(c) 2022-2023 Enderbyte Programs, no rights reserved

Source code at https://github.com/Enderbyte-Programs/Curses-Plus
Available on the Python Package Index

## Sub-Packages List

cursesplus.__init__             A root package with version info, docs, and some base functions

cursesplus.constants            Colour and box-drawing constants.

cursesplus.cp                   The classic (cp 1.x and 2.x) user interface functions

cursesplus.filedialog           Advanced file selection dialogues. (Kept from 2.x)

cursesplus.messagebox           Series of message boxes (like on Windows!)

cursesplus.transitions          Animated transitions module

cursesplus.tuibase              Auto imported. Contains base Window clsses for 3.x

cursesplus.utils                Partially auto imported. Contains misc utility functions and classes that are used frequently

cursesplus.widgets              Auto imported. Contains widget classes for 3.x

NOTICE! CP UTILITIES ARE COMPLETELY INCOMPATIBLE WITH TUIBASE. TO USE THEM, CALL your BaseWindows.screen for the stdscr argument.
"""

__version__ = "3.6.1"
__author__ = "Enderbyte Programs"
__package__ = "cursesplus"

from .tuibase import *
from . import transitions
from . import filedialog
from .widgets import *
from . import cp as classic
from .utils import Coord,set_color,set_colour
from . import messagebox
