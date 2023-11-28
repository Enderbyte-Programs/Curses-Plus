from . import utils,constants
import curses
import random

class Control:
    def __init__(self,parent_window,location:utils.Coord):
        """Initialize a base class for a widget"""
        self.parent = parent_window
        self.location = location
        self.is_selectable = True
        self.control_id = random.randint(1,1000000)#Chances of this leading to issues are literally one in a million
        self.key_events = {}
    def add_key_event(self,keyname:str,func,args=()):
        if not keyname in self.key_events:
            self.key_events[keyname] = []
        self.key_events[keyname].append(utils.CallableFunction(func,args))
    def draw(self):
        """Draw the control on the screen"""
        pass#Required method
    def draw_active(self):
        """Draw the control on the screen"""
        pass#Required method
    def draw_inactive(self):
        """Draw the control on the screen"""
        pass#Required method
    def handle_events(self,key_as_int=-69,key_as_str=b""):
        if self.parent.widgets[self.parent.selected] == self:#Only execute code if I am selected
            if key_as_int == -69 and key_as_str == b"":
                raise TypeError("Provide either the key as an int or string")
            
            if key_as_int != -69:
                activech = curses.keyname(key_as_int)
            else:
                activech = key_as_str

            for kv in list(self.key_events.items()):
                if activech.decode() == kv[0]:
                    for __i in kv[1]:
                        __i.execute()
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
            self.parent.write_raw_text(self.location,self.text,self.colour)
        else:
            self.parent.write_raw_text(self.location,self.text)

class LinkLabel(Control):
    def __init__(self,parent_window,location:utils.Coord,text:str,colour=0):
        super().__init__(parent_window,location)
        self.text = text
        self.is_selectable = True
        self.colour = colour
        self.parent.widgets.append(self)

    def draw_inactive(self):
        if self.colour != 0:
            self.parent.write_raw_text(self.location,self.text,self.colour|curses.A_UNDERLINE)
        else:
            self.parent.write_raw_text(self.location,self.text,curses.A_UNDERLINE)
    def draw_active(self):
        if self.colour != 0:
            self.parent.write_raw_text(self.location,self.text,self.colour|curses.A_UNDERLINE|curses.A_BOLD)
        else:
            self.parent.write_raw_text(self.location,self.text,curses.A_UNDERLINE|curses.A_BOLD)
    def set_activation_function(self,func,args=()):
        """Set what function is called when this object is activated (clicked)"""
        self.remove_key_event("KEY_ENTER")
        self.remove_key_event("^M")
        self.remove_key_event("^J")
        self.add_key_event("KEY_ENTER",func,args)
        self.add_key_event("^M",func,args)
        self.add_key_event("^J",func,args)

class Button(Control):
    def __init__(self,parent_window,location:utils.Coord,text:str):
        super().__init__(parent_window,location)
        self.text = text
        self.is_selectable = True
        self.parent.widgets.append(self)
        self.ic = utils.set_colour(constants.BLACK,constants.WHITE)
        self.ac = utils.set_colour(constants.WHITE,constants.BLACK)
    def set_colour(self,idle_colour,active_colour):
        """Change the colours of the button"""
        self.ic = idle_colour
        self.ac = active_colour
    def draw_inactive(self):
        self.parent.screen.addstr(self.location.y,self.location.x,f"[{self.text}]",self.ic)
    def draw_active(self):
        self.parent.screen.addstr(self.location.y,self.location.x,f"[{self.text}]",self.ac)
    def set_activation_function(self,func,args=()):
        """Set what function is called when this button is clicked"""
        self.add_key_event("KEY_ENTER",func,args)
        self.add_key_event("^M",func,args)
        self.add_key_event("^J",func,args)