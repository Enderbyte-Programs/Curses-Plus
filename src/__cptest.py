import cursesplus
import curses

e = ""
def __test__(stdscr):
    global e
    #cursesplus.textview(stdscr,file="src/cursesplus/cp.py",message="LICENSE",isagreement=True,requireyes=True)
    #e = filedialog.openfiledialog(stdscr)
    cursesplus.transitions.horizontal_bars(stdscr)
    cursesplus.transitions.random_blocks(stdscr)
    cursesplus.transitions.vertical_bars(stdscr)

if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)
    print(e)