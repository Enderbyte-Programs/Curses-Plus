import curses
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