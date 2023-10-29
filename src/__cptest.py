import cursesplus
import curses
import random
import cursesplus.utils
from time import sleep


if __name__ == "__main__":
    win = cursesplus.show_ui()
    win.tui_window.title = "My App"
    win.tui_window.drawWindowBoundary = True
    label1 = cursesplus.widgets.Label(win.tui_window,cursesplus.utils.Coord(1,1),"Hello World!",colour=cursesplus.utils.set_colour(curses.COLOR_BLACK,curses.COLOR_GREEN)|curses.A_UNDERLINE)
    win.update()
    win.screen.getch()
    cursesplus.shutdown_ui()