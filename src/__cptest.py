import cursesplus
import curses
import random
e = ""
e2 = ""
e3 = ""
def __test__(stdscr):
    f = ""
    #cursesplus.date_time_selector(stdscr,cursesplus.DateTimeSelectorTypes.DATEANDTIME,"When were you born?",True,False)
    ops = [str(random.randint(0,100000)) for i in range(100)]
    print(cursesplus.searchable_option_menu(stdscr,ops,"select something"))
if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)
    print(e,e2,e3)