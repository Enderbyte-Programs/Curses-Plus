from . import utils

class Control:
    def __init__(self,parent_window,location:utils.Coord):
        """Initialize a base class for a widget"""
        self.parent = parent_window
        self.location = location
    def draw(self):
        """Draw the control on the screen"""
        pass#Required method

class Label(Control):
    def __init__(self,parent_window,location:utils.Coord,text:str,colour=0):
        super().__init__(parent_window,location)
        self.text = text
        self.colour = colour
        self.parent.widgets.append(self)
    def draw(self):
        if self.colour != 0:
            self.parent.screen.addstr(self.location.y,self.location.x,self.text,self.colour)
        else:
            self.parent.screen.addstr(self.location.y,self.location.x,self.text)