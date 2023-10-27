import curses
import os
from . import messagebox,utils
import signal
import sys

id_ind = 0
def get_new_winid() -> int:
    global id_ind
    id_ind += 1
    return id_ind

class AlreadyInitializedError(Exception):
    def __init__(self,message):
        self.message = message

class BaseWindow:
    """A class for the base terminal. You may only use this once. To interface with this as if it were a window, use (self).tui_window which is a Window object set to the bounds of the screen."""
    def __init__(self,screen):
        global __SCREEN
        self.screen = screen
        self.children: list[Window] = []
        __SCREEN = screen
        self.size_x, self.size_y = os.get_terminal_size()
        self.size_y -= 2
        self.size_x -= 1
        self.tui_window = Window(self,self.screen,self.size_x,self.size_y,0,0)
        self.tui_window.drawWindowBoundary = False
        self.tui_window.title = "Application"
        
        #self.tui_window.update()
    def create_child_window(self,offset:utils.Coord,size:utils.Coord):
        """Create and return a window object"""
        return Window(self,self.screen,size.x,size.y,offset.x,offset.y)
    def update(self):
        """Update and refresh the screen"""
        for w in self.children:
            w.update()
        self.screen.refresh()

class Window:
    drawWindowBoundary = True
    def __init__(self,parent:BaseWindow,screen,size_x: int,size_y:int,offset_x:int,offset_y:int,window_title="Window"):
        self.screen: curses._CursesWindow = screen
        self.parent: BaseWindow = parent
        self.title = window_title
        self.id = get_new_winid()
        self.size_coords = utils.Coord(size_x,size_y)
        self.offset_coords = utils.Coord(offset_x,offset_y)
        self.parent.children.append(self)
        #signal.signal(signal.SIGINT,__base_signal_handler)#Register base shutdown
    def update(self):
        if self.drawWindowBoundary:
            utils.draw_bold_rectangle(self.screen,self.offset_coords,self.size_coords+self.offset_coords)
            self.screen.addstr(self.offset_coords.y,self.offset_coords.x+2,utils.constants.DOUBLE_HORIZ_TRUNC_LEFT+self.title+utils.constants.DOUBLE_HORIZ_TRUNC_RIGHT)
        self.screen.refresh()
    def write_raw_text(self,location:utils.Coord,string:str,colour=0):
        if colour != 0:
            self.screen.addstr(location.y,location.x,string,colour)
        else:
            self.screen.addstr(location.y,location.x,string)

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
    curses.reset_shell_mode()
    curses.endwin()
    sys.exit()

def __base_signal_handler(signal,frame):
    if messagebox.askyesno(stdscr,["Are you sure you wish to exit?"]):
        stdscr.erase()
        shutdown_ui()
        #sys.exit()
