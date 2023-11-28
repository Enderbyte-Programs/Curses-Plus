import sys
import cursesplus
import curses
import random
import cursesplus.utils
import webbrowser
from time import sleep

def say_hi(screen):
    global win
    win.remove_key_event(curses.keyname(curses.KEY_DOWN))
    cursesplus.messagebox.showinfo(screen,["Hello, world!"])
money = 0
def generate() -> bool:
    global button1
    global win
    global money
    r = [100,200,500,0]
    l = random.choice(r)
    if l == 0:
        money = 0
        cursesplus.messagebox.showinfo(win.get_underlying_window().screen,["ALARM!!!"])
        button1.text = f"You have {money} money"
        return False
    else:
        money += l
        button1.text = f"You have {money} money"
if __name__ == "__main__":
    win = cursesplus.show_ui()
    win.set_title("Beat The Bank")
    win.show_boundary()
    win2 = win.create_child_window(cursesplus.Coord(10,10),cursesplus.Coord(10,10))
    win2.drawWindowBoundary = True
    win2.title = "Settings"
    label1 = cursesplus.widgets.Label(win.get_underlying_window(),cursesplus.Coord(1,1),"Welcome to Beat The bank. Select Go! to begin")
    button1 = cursesplus.widgets.Label(win.get_underlying_window(),cursesplus.Coord(1,2),f"You have {money} money")
    button = cursesplus.widgets.Button(win.get_underlying_window(),cursesplus.Coord(1,3),"Go!")
    button.set_colour(cursesplus.set_colour(cursesplus.constants.BLACK,cursesplus.constants.GREEN),cursesplus.set_colour(cursesplus.constants.GREEN,cursesplus.constants.BLACK))
    button.set_activation_function(generate)
    button2 = cursesplus.widgets.Button(win.get_underlying_window(),cursesplus.Coord(1,5),"Exit")
    button2.set_activation_function(win.shut_up_ui_loop)
    win.get_underlying_window().set_first_selected(button)
    #win.get_underlying_window().set_cycle_keys(b'KEY_DOWN',b'KEY_UP')
    win.start_ui_loop()

    cursesplus.shutdown_ui()