from . import utils
import curses

class Control:
    def __init__(self,parent_window,location:utils.Coord):
        """Initialize a base class for a widget"""
        self.parent = parent_window
        self.location = location
        self.is_selectable = True
        self.key_events = {}
    def add_key_event(self,keyname:str,func,args=()):
        self.key_events[keyname] = utils.CallableFunction(func,args)
    def draw(self):
        """Draw the control on the screen"""
        pass#Required method
    def handle_events(self,key_as_int=-69,key_as_str=""):
        if key_as_int == -69 and key_as_str == "":
            raise TypeError("Provide either the key as an int or string")
        
        if key_as_int != -69:
            activech = curses.keyname(key_as_int)
        else:
            activech = key_as_str

        for kv in list(self.key_events.items()):
            if activech == kv[0]:
                kv[1].execute()
    def remove_key_event(self,key_to_remove):
        """Remove any functions registered to `key_to_remove`"""
        try:
            del self.key_events[key_to_remove]
        except:
            pass

class Label(Control):
    def __init__(self,parent_window,location:utils.Coord,text:str,colour=0):
        super().__init__(parent_window,location)
        self.text = text
        self.is_selectable = False
        self.colour = colour
        self.parent.widgets.append(self)
    def draw(self):
        if self.colour != 0:
            self.parent.screen.addstr(self.location.y,self.location.x,self.text,self.colour)
        else:
            self.parent.screen.addstr(self.location.y,self.location.x,self.text)