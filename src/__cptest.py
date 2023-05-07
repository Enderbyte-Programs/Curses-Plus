from cursesplus import *
from cursesplus import filedialog
import cursesplus
import cursesplus.messagebox
from time import sleep

def __test__(stdscr):
    filedialog.openfilesdialog(stdscr)
    showcursor()
if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)