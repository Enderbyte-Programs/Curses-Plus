import cursesplus
import curses
import random
e = ""
def __test__(stdscr):
    global e
    #cursesplus.textview(stdscr,file="src/cursesplus/cp.py",message="LICENSE",isagreement=True,requireyes=True)
    #e = cursesplus.filedialog.openfiledialog(stdscr,allowcancel=False)
    #cursesplus.coloured_option_menu(stdscr,["Hello","I am Jordan","bAcK"])
    #cursesplus.messagebox.showinfo(stdscr,["Hello","This is a message for you"],"Message")
    e = cursesplus.checkboxlist(stdscr,[
        cursesplus.CheckBoxItem("dtk","Show Desktop Icon",False),
        cursesplus.CheckBoxItem("rfm","Register File Association",True),
        cursesplus.CheckBoxItem("smm","Create Start Meny Icon",True)
    ],"Choose optional features for installation",2,3)
    #cursesplus.textview(stdscr,file="/home/jordan/Coding/cursesplus/src/cursesplus/cp.py")
    #cursesplus.cursesinput(stdscr,"Hello",bannedcharacters="")
if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)
    print(e)