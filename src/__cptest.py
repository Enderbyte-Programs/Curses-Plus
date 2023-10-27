import cursesplus
import curses
import random
import cursesplus.utils
from time import sleep
if __name__ == "__main__":
    win = cursesplus.show_ui()
    subwin = win.create_child_window(cursesplus.Coord(5,5),cursesplus.Coord(10,5))
    subwin.drawWindowBoundary = True
    subwin.update()
    #cursesplus.utils.draw_bold_rectangle(subwin.screen,cursesplus.Coord(5,5),cursesplus.Coord(10,10))
    win.update()
    win.screen.getch()
    cursesplus.shutdown_ui()