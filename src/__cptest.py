from cursesplus import *
from cursesplus import filedialog
import cursesplus
import cursesplus.messagebox
from time import sleep

def __test__(stdscr):
    displaymsg(stdscr,[filedialog.openfolderdialog(stdscr)])
if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)