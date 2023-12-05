import cursesplus
import curses
import random
e = ""
def __test__(stdscr):
    global e
    #cursesplus.textview(stdscr,file="src/cursesplus/cp.py",message="LICENSE",isagreement=True,requireyes=True)
    #e = cursesplus.filedialog.openfiledialog(stdscr,allowcancel=False)
    cursesplus.coloured_option_menu(stdscr,["Hello","I am Jordan","bAcK"],footer="Hello Everyone!")
    #cursesplus.messagebox.showinfo(stdscr,["Hello","This is a message for you"],"Message")
    #cursesplus.textview(stdscr,file="/home/jordan/Coding/cursesplus/src/cursesplus/cp.py")
    #cursesplus.cursesinput(stdscr,"Hello",bannedcharacters="")
    cursesplus.messagebox.askyesno(stdscr,["Hi. I am Jordan Rahim"],default=cursesplus.messagebox.MessageBoxStates.NO)
if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)
    print(e)