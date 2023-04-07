import curses#Depends on windows-curses on win32
from curses.textpad import rectangle, Textbox
import os
from time import sleep
import random
from datetime import datetime

#DEFINE SOME CONSTANTS
BLACK = curses.COLOR_BLACK
WHITE = curses.COLOR_WHITE
RED = curses.COLOR_RED
YELLOW = curses.COLOR_YELLOW
GREEN = curses.COLOR_GREEN
CYAN = curses.COLOR_CYAN
BLUE = curses.COLOR_BLUE
MAGENTA = curses.COLOR_MAGENTA

_C_INIT = False

def cursestransition(stdscr,func_to_call=None,args=(),type=0):
    """
    Generate a fancy transition with curses. Type 0 is a wipe transition with lines. Type 1 is a more powerful random block pixel transition.
    Calls func_to_call(args) after transition is finishd
    """
    block = "█"
    mx,my = os.get_terminal_size()
    if type == 0:
        
        for y in range(my-1):
            stdscr.addstr(y,0,block*(mx-1))
            stdscr.refresh()
            sleep(0.01)
        for y in range(my-1):
            stdscr.addstr(y,0," "*(mx-1))
            stdscr.refresh()
            sleep(0.01)
    elif type == 1:
        _grid = [(x,y) for y in range(my-1) for x in range(mx-1)]
        while _grid:
            for i in range(round(((my*mx)/(24*80))*20)):# Fixing slow transitions on HD screens
                try:
                    pk = random.choice(_grid)
                    _grid.pop(_grid.index(pk))
                    stdscr.addstr(pk[1],pk[0],block)
                    stdscr.refresh()
                except:
                    break
            sleep(0.01)
        _grid = [(x,y) for y in range(my-1) for x in range(mx-1)]
        while _grid:
            for i in range(round(((my*mx)/(24*80))*20)):
                try:
                    pk = random.choice(_grid)
                    _grid.pop(_grid.index(pk))
                    stdscr.addstr(pk[1],pk[0]," ")
                    stdscr.refresh()
                except:
                    break
            sleep(0.01)
    if func_to_call is not None:
        func_to_call(*args)
def displaymsg(stdscr,message: list):
    """
    Display a message in a rectangle. Stdscr is the screen and message is a list. Each item in the list is a new line. For a single line message call displaymsg(stdscr,["message here"])
    Message will be dismissed when a key is pressed.
    """
    stdscr.clear()
    x,y = os.get_terminal_size()
    ox = 0
    for o in message:
        ox += 1
        if "\n" in o:
            message.insert(ox,o.split("\n")[1])
    message = [m[0:x-5].split("\n")[0] for m in message]#Limiting characters
    maxs = max([len(s) for s in message])
    rectangle(stdscr,y//2-(len(message)//2)-1, x//2-(maxs//2)-1, y//2+(len(message)//2)+2, x//2+(maxs//2+1)+1)
    stdscr.addstr(0,0,"Message: ")
    mi = -(len(message)/2)
    
    for msgl in message:
        mi += 1
        stdscr.addstr(int(y//2+mi),int(x//2-len(msgl)//2),msgl)
    stdscr.addstr(y-2,0,"Press any key to dismiss this message")
    stdscr.refresh()
    stdscr.getch()
    stdscr.erase()

def displaymsgnodelay(stdscr,message: list):
    """
    Display a message in a rectangle. message is a list. Each item in the list is a new line. Unlike displaymsg, the message will not need a keypress to continue. This is good for progress waiing.
    """
    stdscr.clear()
    x,y = os.get_terminal_size()
    ox = 0
    for o in message:
        ox += 1
        if "\n" in o:
            message.insert(ox,o.split("\n")[1])
    message = [m[0:x-5].split("\n")[0] for m in message]#Limiting characters
    maxs = max([len(s) for s in message])
    rectangle(stdscr,y//2-(len(message)//2)-1, x//2-(maxs//2)-1, y//2+(len(message)//2)+2, x//2+(maxs//2+1)+1)
    stdscr.addstr(0,0,"Message: ")
    mi = -(len(message)/2)
    
    for msgl in message:
        mi += 1
        stdscr.addstr(int(y//2+mi),int(x//2-len(msgl)//2),msgl)
    stdscr.refresh()
    stdscr.erase()

def cursesinput(stdscr,prompt: str):
    """
    Get a single line input of text from curses. To be used instead of Python standard input()
    """
    x,y = os.get_terminal_size()
    stdscr.erase()
    stdscr.addstr(0, 0, f"{prompt} (hit Enter to send)")

    editwin = curses.newwin(1,x-2, 2,1)
    rectangle(stdscr, 1,0, 3, x-1)
    stdscr.refresh()

    box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()
    return message[0:-1]

def displayops(stdscr,options: list,title="Please choose an option") -> int:
    """Display an options menu provided by options list. ALso displays title. Returns integer value of selected item."""
    mx, my = os.get_terminal_size()
    selected = 0
    
    options = [l[0:mx-3] for l in options]
    maxlen = max([len(l) for l in options])
    stdscr.addstr(0,0,title[0:mx-1])
    offset = 0
    while True:
        stdscr.addstr(0,0,title[0:mx-1])
        mx, my = os.get_terminal_size()
        options = [l[0:mx-3] for l in options]
        maxlen = max([len(l) for l in options])
        if len(options) > my-5:
            rectangle(stdscr,1,0,my-2,mx-1)
        else:
            rectangle(stdscr,1,0,2+len(options),maxlen+2)
        oi = -1
        for o in options[offset:offset+(my-4)]:
            oi += 1
            try:
                if oi == selected-offset:
                    stdscr.addstr(oi+2,1,o,set_colour(WHITE,BLACK))
                else:
                    stdscr.addstr(oi+2,1,o)
            except curses.error:
                pass
        stdscr.addstr(my-1,0,"Please choose an option with the arrow keys then press enter."[0:mx-1])
        stdscr.refresh()
        _ch = stdscr.getch()
        if _ch == curses.KEY_ENTER or _ch == 10 or _ch == 13:
            return selected
        elif _ch == curses.KEY_UP and selected > 0:
            if offset > 0 and selected-offset == 0:
                offset -= 1
            selected -= 1
        elif _ch == curses.KEY_DOWN and selected < len(options)-1:
            if selected >= my-6:
                offset += 1
            selected += 1
        elif _ch == curses.KEY_BACKSPACE or _ch == 98:
            return -1
        stdscr.erase()
def optionmenu(stdscr,options:list,title="Please choose an option and press enter") -> int:
    """Alias function to displayops()"""
    return displayops(stdscr,options,title)

def askyesno_old(stdscr,title: str) -> bool:
    """Ask a yes no question provided by title."""
    result = displayops(stdscr,["Yes","No"],title)
    if result == 0:
        return True
    else:
        return False
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

def displayerror(stdscr,e,msg: str):
    """
    Display an error message
    """
    displaymsg(stdscr,["An error occured",msg,str(e)])

def filline(stdscr,line: int,colour: int):
    """Fill a line, colour is the result of set_colour(fg,bg)"""
    stdscr.addstr(line,0," "*(os.get_terminal_size()[0]-1),colour)

def hidecursor():
    """Hide Cursor. Can only be called in an active curses window"""
    curses.curs_set(0)

def showcursor():
    """Show cursor. Can only be called in an active curses window"""
    curses.curs_set(1)

class ProgressBar:
    def __init__(self,stdscr,max_value: int, step_value=1,show_percent=True,show_log=False,message="Progress",waitforkeypress=False):
        """Display a Progress Bar with a log. Good for install progresses"""
        self.screen = stdscr
        self.max = max_value
        self.stepval = step_value
        self.sp = show_percent
        self.sl = show_log
        self.msg = message
        self.ACTIVE = False
        self.value = 0
        self.loglist: list[str] = []
        self.lclist: list[int] = []
        self.submsg = ""
        self.mx, self.my = os.get_terminal_size()
        self.wfkp = waitforkeypress
    def update(self):
        lheight = self.my - 7
        """Redraws progress bar"""
        self.screen.erase()
        self.screen.addstr(0,0," "*(self.mx-1),set_colour(BLUE,WHITE))
        self.screen.addstr(0,0,self.msg[0:self.mx-1],set_colour(BLUE,WHITE))
        #filline(self.screen,1,set_colour(GREEN,WHITE))
        filline(self.screen,2,set_colour(RED,WHITE))
        #filline(self.screen,3,set_colour(GREEN,WHITE))
        self.screen.addstr(1,0,"-"*(self.mx-1),set_colour(RED,WHITE))
        self.screen.addstr(3,0,"-"*(self.mx-1),set_colour(RED,WHITE))
        barfill = round((self.value/self.max)*self.mx-1)
        if not self.value > self.max:
            self.screen.addstr(2,0," "*barfill,set_colour(GREEN,WHITE))
        else:
            self.screen.addstr(2,0," "*self.mx-1,set_colour(GREEN,WHITE))
        self.screen.addstr(3,0,self.submsg[0:self.mx-1],set_colour(RED,WHITE))
        if self.sp:
            self.screen.addstr(3,self.mx-7,f"{round(self.value/self.max*100,1)} %",set_colour(RED,WHITE))
        if self.sl:
            rectangle(self.screen,4,0,self.my-2,self.mx-1)
            if len(self.loglist) > lheight:
                lx = 0
                for val in self.loglist[len(self.loglist)-lheight:]:
                    self.screen.addstr(lx+5,1,val[0:self.mx-2],self.lclist[len(self.loglist)-lheight+lx])
                    lx += 1
            else:
                lx = 0
                for val in self.loglist:
                    self.screen.addstr(lx+5,1,val[0:self.mx-2],self.lclist[lx])
                    lx += 1
        self.screen.refresh()
    def step(self,message: str = "",addmsgtolog:bool = False):
        """Perform step of self.stepval (default 1). Sets message to message. Optionally adds message to log"""
        self.value += self.stepval
        self.submsg = message
        if addmsgtolog:
            self.appendlog(message)
        self.update()
    def done(self):
        """Mark progress bar as complete. Optionally waits for keypress. Control with self.wfkp(bool)"""
        if self.wfkp:
            self.value = self.max
            self.submsg = "Press any key to continue"
            self.update()
            self.screen.getch()
        self.screen.clear()
    def appendlog(self,text: str,colour: int = 0):
        """Add text to log with colour colour"""
        self.loglist.append(text)
        self.lclist.append(colour)
        self.update() 