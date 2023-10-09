import cursesplus
import curses
import random
e = ""
def __test__(stdscr):
    global e
    cursesplus.textview(stdscr,file="src/cursesplus/cp.py",message="LICENSE",isagreement=True,requireyes=True)
    #e = filedialog.openfiledialog(stdscr)
    #e = cursesplus.checkboxlist(stdscr,{"Create Desktop Shortcut":False,"Create Start Menu Shortcut":True,"Register MIME type":True},"Choose optional features for installation",2,3)
    #cursesplus.textview(stdscr,file="/home/jordan/Coding/cursesplus/src/cursesplus/cp.py")
    cursesplus.cursesinput(stdscr,"Hello",bannedcharacters="")
if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)
    print(e)