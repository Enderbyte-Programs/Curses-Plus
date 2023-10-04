import cursesplus
import curses
import random
e = ""
def __test__(stdscr):
    global e
    #cursesplus.textview(stdscr,file="src/cursesplus/cp.py",message="LICENSE",isagreement=True,requireyes=True)
    #e = filedialog.openfiledialog(stdscr)
    cursesplus.coloured_option_menu(stdscr,["Back","Start","Bye"],"Hello",[["start",cursesplus.GREEN]])
    cursesplus.cursesinput(stdscr,"Hello",bannedcharacters="a,b")

if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)
    print(e)