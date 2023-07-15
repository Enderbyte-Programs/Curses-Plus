from cursesplus import *
from cursesplus import filedialog
import cursesplus
import cursesplus.messagebox
from time import sleep

e = ""
def __test__(stdscr):
    global e
    #e = cursesinput(stdscr,"Hello",5,50,prefiltext="This is a single line prefil",retremptylines=True).splitlines()
    e = cursesplus.messagebox.askokcancel(stdscr,["Do you want to die?"])
    pw = PleaseWaitScreen(stdscr)
    pw.start()
    sleep(5)
    pw.stop()
    pw.destroy()

if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)
    print(e)