from cursesplus import *
from cursesplus import filedialog
import cursesplus
import cursesplus.messagebox
from time import sleep

def __test__(stdscr):
    displaymsg(stdscr,[filedialog.openfolderdialog(stdscr)])
    p = ProgressBar(stdscr,100,bar_location=ProgressBarLocations.CENTER)
    for i in range(100):
        sleep(0.1)
        p.step(str(i))
    p.done()
if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)