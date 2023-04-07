from cursesplus import *
from cursesplus import filedialog
import cursesplus
import cursesplus.messagebox
from time import sleep

def __test__(stdscr):
    hidecursor()
    optionmenu(stdscr,[str(i) for i in range(1000)],"Hello!")
    p = ProgressBar(stdscr,1000,1,show_log=True)
    for i in range(1000):
        p.step(str(i),True)
        #sleep(0.1)
    cursesplus.messagebox.showwarning(stdscr,["This is a","WARNING!"])
    filedialog.openfiledialog(stdscr)
    showcursor()
if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)