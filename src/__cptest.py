import cursesplus
import curses
import random
e = ""
e2 = ""
e3 = ""
def __test__(stdscr):
    f = ""
    for i in range(10000):
        f += random.choice(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))
    cursesplus.textview(stdscr,text=f)
if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)
    print(e,e2,e3)