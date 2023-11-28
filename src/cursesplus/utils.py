import curses
from . import constants
class Coord:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def as_tuple(self) -> tuple:
        return (self.x,self.y)
    def as_inverted_tuple(self) -> tuple:
        return (self.y,self.x)
    def __add__(self,other):
        if not isinstance(other,Coord):
            raise TypeError("Must be Coord type")
        else:
            return Coord(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        if not isinstance(other,Coord):
            raise TypeError("Must be Coord type")
        else:
            return Coord(self.x-other.x,self.y-other.y)
_C_INIT = False
def retr_nbl_lst(input:list)->list:
    return [l for l in input if str(l) != ""]  
def calc_nbl_list(input:list)->int:
    x = 0
    for ls in input:
        x += len(ls)
    return x

def str_contains_word(s:str,string:str) -> bool:
    d = s.lower().split(" ")
    return string in d

def list_get_maxlen(l:list) -> int:
    return max([len(s) for s in l])

_AVAILABLE_COL = list(range(1,255,1))
_COL_INDEX = {}
def set_colour(background: int, foreground: int) -> int:
    global _C_INIT
    global _COL_INDEX
    global _AVAILABLE_COL
    """Set a colour object. Use the constants provided. z
    For attributes use | [ATTR] for example set_colour(RED,GREEN) | sdf
    """
    if not _C_INIT:
        curses.start_color()
        curses.use_default_colors()
        _C_INIT = True

    if str(foreground) in _COL_INDEX.keys() and str(background) in _COL_INDEX[str(foreground)].keys():
        return curses.color_pair(_COL_INDEX[str(foreground)][str(background)])
    if len(_AVAILABLE_COL) == 0:
        raise Warning("Out of colours!")
        _AVAILABLE_COL = list(range(1,255,1))#Replenish list
    i = _AVAILABLE_COL.pop(0)
    curses.init_pair(i,foreground,background)
    if not str(foreground) in _COL_INDEX.keys():
        _COL_INDEX[str(foreground)] = {}
    _COL_INDEX[str(foreground)][str(background)] = i
    return curses.color_pair(i)

def set_color(background: int,foreground: int) -> int:
    return set_colour(background,foreground)

def draw_bold_rectangle(stdscr,ulc:Coord,brc:Coord):
    stdscr.addstr(ulc.y,ulc.x,constants.DOUBLE_TL_CORNER)
    stdscr.addstr(ulc.y,brc.x,constants.DOUBLE_TR_CORNER)
    stdscr.addstr(brc.y,ulc.x,constants.DOUBLE_BL_CORNER)
    stdscr.addstr(brc.y,brc.x,constants.DOUBLE_BR_CORNER)
    stdscr.addstr(ulc.y,ulc.x+1,constants.DOUBLE_HORIZ*(brc.x-ulc.x-1))
    stdscr.addstr(brc.y,ulc.x+1,constants.DOUBLE_HORIZ*(brc.x-ulc.x-1))
    #stdscr.addstr(ulc.y+1,ulc.x,constants.DOUBLE_VERT*(brc.y - ulc.y-2))
    #stdscr.addstr(ulc.y+1,brc.x,constants.DOUBLE_VERT*(brc.y - ulc.y-2))
    for ln in range(ulc.y+1,brc.y,1):
        stdscr.addstr(ln,ulc.x,constants.DOUBLE_VERT)
        stdscr.addstr(ln,brc.x,constants.DOUBLE_VERT)

class CallableFunction:
    """A function. Not for use by end-users"""
    def __init__(self,func,args=()):
        self.function = func
        self.arguments = args
    def execute(self):
        return self.function(*self.arguments)
