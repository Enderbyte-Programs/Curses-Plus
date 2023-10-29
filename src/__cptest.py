import cursesplus
import curses
import random
import cursesplus.utils
from time import sleep

def say_hi(screen):
    global win
    win.remove_key_event(curses.keyname(curses.KEY_DOWN))
    cursesplus.messagebox.showinfo(screen,["Hello, world!"])

if __name__ == "__main__":
    win = cursesplus.show_ui()
    win.set_title("My App")
    win.show_boundary()
    label1 = cursesplus.widgets.Label(win.tui_window,cursesplus.utils.Coord(1,1),"Hello World!",colour=cursesplus.utils.set_colour(curses.COLOR_BLACK,curses.COLOR_GREEN)|curses.A_UNDERLINE)
    win.add_key_event(curses.keyname(curses.KEY_DOWN),say_hi,(win.screen,))
    win.add_key_event(curses.keyname(curses.KEY_UP),win.shut_up_ui_loop)
    win.start_ui_loop()

    cursesplus.shutdown_ui()