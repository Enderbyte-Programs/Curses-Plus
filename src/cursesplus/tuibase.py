import curses
import os
from .constants import *
__SCREEN = None
class AlreadyInitializedError(Exception):
    def __init__(self,message):
        self.message = message

class Coord:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def as_tuple(self) -> tuple:
        return (self.x,self.y)
    def as_inverted_tuple(self) -> tuple:
        return (self.y,self.x)

class BaseWindow:
    
    def __init__(self,screen):
        global __SCREEN
        self.screen = screen
        __SCREEN = screen
        self.size_x, self.size_y = os.get_terminal_size()
        self.size_x -= 1

class Window:
    def __init__(self,parent:BaseWindow,screen,size_x,size_y):
        self.screen = screen
        self.parent: BaseWindow = parent
        self.size_x = size_x
        self.size_y = size_y
        self.maximum_coords = Coord(size_x,size_y)

def show_ui() -> BaseWindow:  
    """Start the user interface. Returns a BaseWindow you can use for editing"""
    global stdscr
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    stdscr.keypad(True)
    return BaseWindow(stdscr)

def shutdown_ui():
    """Shut down the UI and return the terminal to its normal state"""
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()