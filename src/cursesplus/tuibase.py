import curses
import os
from . import messagebox,utils,widgets
import sys

id_ind = 0
def get_new_winid() -> int:
    global id_ind
    id_ind += 1
    return id_ind

class AlreadyInitializedError(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.message = message

class BaseWindow:
    """A class for the base terminal. You may only use this once. To interface with this as if it were a window, use (self).tui_window or (self).get_underlying_window() which is a Window object set to the bounds of the screen."""
    def __init__(self,screen):
        global __SCREEN
        self.screen = screen
        self.children: list[Window] = []
        __SCREEN = screen
        self.size_x, self.size_y = os.get_terminal_size()
        self.size_y -= 2
        self.size_x -= 1
        
        self.haltuiloop = False
        self.master_key_events = {}

        self.tui_window = Window(self,self.screen,self.size_x,self.size_y,0,0)
        self.tui_window.drawWindowBoundary = False
        self.tui_window.title = "Application"
        self.selected_id = 1
        
        #self.tui_window.update()
    def add_key_event(self,keyname:str,func,args=()):
        """Add a new key event. A key event is a functiom that is called when a key is pressed."""
        if not keyname in self.master_key_events:
            self.master_key_events[keyname] = []
        self.master_key_events[keyname].append(utils.CallableFunction(func,args))
    def remove_key_events(self,keyname:str):
        """Remove all events associated to keyname"""
        try:
            del self.master_key_events[keyname]
        except:
            pass
    def _cycle(self):
        """Cycle through active windows"""
        self.children[self.selected_id-1].is_selected = False
        if self.selected_id == len(self.children):
            self.selected_id = 1

        self.children[self.selected_id-1] = True
    def handle_key_events(self,keyname:str):
        """Do all global key events based on the provided keyname"""
        for c in list(self.master_key_events.items()):
            if c[0] == keyname:
                for __x in c[1]:
                    __x.execute()
    def create_child_window(self,offset:utils.Coord,size:utils.Coord):
        """Create and return a new child Window object to your specification"""
        return Window(self,self.screen,size.x,size.y,offset.x,offset.y)
    def update(self):
        """Update and refresh the screen"""
        for w in self.children:
            w.update()
        self.screen.refresh()
    def update_keyevents(self,key:str):
        """Execute key event updates for all child windows"""
        self.handle_key_events(key)
        for w in self.children:
            w.upadte_keyevents(key)
    def shut_up_ui_loop(self):
        """Shut down the UI loop"""
        self.haltuiloop = True
    def set_title(self,new_title:str):
        """Change the master window title"""
        self.tui_window.title = new_title
    def get_title(self) -> str:
        return self.tui_window.title
    def get_underlying_window(self):
        """Return this window as a WindowObject. Must be used for putting widgets on to the base screen"""
        return self.tui_window
    def show_boundary(self):
        """Show the Window Boundary and title on the master window"""
        self.tui_window.drawWindowBoundary = True
    def hide_boundary(self):
        """Do not display the window boundary and title on the master window"""
        self.tui_window.drawWindowBoundary = False
    def start_ui_loop(self):
        """Start an infinite loop of updating the UI on a keypress"""
        while not self.haltuiloop:
            self.update()
            ch = curses.keyname(self.screen.getch())
            self.update_keyevents(ch)
            self.screen.clear()
        self.haltuiloop = False#Reset so it is good for next time
    def remove_key_event(self,key_to_remove):
        """Remove any functions registered to `key_to_remove`"""
        try:
            del self.master_key_events[key_to_remove]
        except:
            pass

def intkey_to_keyname(i:int) -> bytes:
    return curses.keyname(i)

class Window:
    drawWindowBoundary = True
    def __init__(self,parent:BaseWindow,screen,size_x: int,size_y:int,offset_x:int,offset_y:int,window_title="Window"):
        self.screen: curses._CursesWindow = screen
        self.parent: BaseWindow = parent
        self.title = window_title
        self.id = get_new_winid()
        self.widgets: list[widgets.Control] = []
        self.size_coords = utils.Coord(size_x,size_y)
        self.offset_coords = utils.Coord(offset_x,offset_y)
        self.parent.children.append(self)
        self.selected = 0
        self.is_selected = False
        self.set_cycle_keys(b'KEY_SLEFT',b'KEY_SRIGHT')
        #signal.signal(signal.SIGINT,__base_signal_handler)#Register base shutdown
    def set_cycle_keys(self,descend:bytes,ascend:bytes):
        """Set the keys (string representation) (so the result of cursesplus.intkey_to_keyname"""
        self.parent.add_key_event(descend,self._incsel)
        self.parent.add_key_event(ascend,self._decsel)
    def _get_cyclable_widgets(self) -> list:
        return [s for s in self.widgets if s.is_selectable]
    def set_first_selected(self,widget:widgets.Control):
        """Set the currently selected item to the widget provided"""
        pi = 0
        rpi = self.selected
        dn = 0
        for item in self.widgets:
            if item == widget:
                dn = 1
                self.selected = pi
            pi += 1
        if dn == 0:
            self.selected = rpi
            raise Warning("The provided widget to select does not exist in the window")
    def _incsel(self):
        if len(self._get_cyclable_widgets() <= 1):
            return#Cancel if only one widget
        self.selected += 1
        while True:
            if self.selected > len(self.widgets)-1:
                self.selected = len(self.widgets)-1
                return
            if not self.widgets[self.selected].is_selectable:
                self.selected += 1
                
            else:
                break
    def _every_widget_before_here_is_not_selectable(self,ind) -> bool:
        e = True
        for j in self.widgets[0:ind]:
            if j.is_selectable:
                e = False
        return e
    def _decsel(self):
        if len(self._get_cyclable_widgets() <= 1):
            return#Cancel if only one widget
        if self.selected == 0:
            return
        if self.selected > len(self.widgets)-1:
            self.selected = len(self.widgets)-1
        self.selected -= 1
        while True:
            if not self.widgets[self.selected].is_selectable and self._every_widget_before_here_is_not_selectable(self.selected):
                self.selected += 1
                return
            if not self.widgets[self.selected].is_selectable:
                self.selected -= 1
            else:
                break
        
    def update(self):
        if self.drawWindowBoundary:
            utils.draw_bold_rectangle(self.screen,self.offset_coords,self.size_coords+self.offset_coords)
            self.screen.addstr(self.offset_coords.y,self.offset_coords.x+2,utils.constants.DOUBLE_HORIZ_TRUNC_LEFT+self.title+utils.constants.DOUBLE_HORIZ_TRUNC_RIGHT)
        ci = 0
        for c in self.widgets:
            if not c.is_selectable:
                c.draw()
            else:
                if ci == self.selected:
                    c.draw_active()
                else:
                    c.draw_inactive()
            ci += 1

        self.screen.refresh()
    def upadte_keyevents(self,key):
        for c in self.widgets:
            c.handle_events(key_as_str=key)
    def write_raw_text(self,location:utils.Coord,string:str,colour=0):
        if colour != 0:
            self.screen.addstr(location.y+self.offset_coords.y,location.x+self.offset_coords.x,string,colour)
        else:
            self.screen.addstr(location.y+self.offset_coords.y,location.x+self.offset_coords.x,string)

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
