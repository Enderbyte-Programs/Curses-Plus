import cursesplus
import curses
import random
e = ""
e2 = ""
e3 = ""
def __test__(stdscr):
    global e
    global e2
    global e3
    e = cursesplus.date_time_selector(stdscr,cursesplus.DateTimeSelectorTypes.DATEONLY,"When were you born",True,False)
    #Tests DateOnly and past only
    e2 = cursesplus.date_time_selector(stdscr,cursesplus.DateTimeSelectorTypes.TIMEONLY,"What time do you go to school",True,True)
    #Tests TimeOnly and allow all
    e3 = cursesplus.date_time_selector(stdscr,cursesplus.DateTimeSelectorTypes.DATEANDTIME,"Choose something in future",False,True)
if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)
    print(e,e2,e3)