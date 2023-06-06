from cursesplus import *
from cursesplus import filedialog
import cursesplus
import cursesplus.messagebox
from time import sleep

def __test__(stdscr):
    cursesplus.messagebox.showinfo(stdscr,cursesinput(stdscr,"Hello",5,50).splitlines())
if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)