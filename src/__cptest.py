from cursesplus import *
from cursesplus import filedialog
import cursesplus
import cursesplus.messagebox
from time import sleep

e = ""
def __test__(stdscr):
    global e
    #e = cursesinput(stdscr,"Hello",5,50,prefiltext="This is a single line prefil",retremptylines=True).splitlines()
    e = numericinput(stdscr,"What is your favourite number?",False,False,10,1000)

if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)
    print(e)